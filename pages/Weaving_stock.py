import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
import base64
from io import BytesIO

# def Stock():
warnings.filterwarnings("ignore")


st.set_page_config(page_title="Weaving Stock", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Weaving Stock Details - All Mills")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)


# Load your data
df = pd.read_excel("weaving_stock.xlsx",skiprows=6)


# Assuming `df` is your DataFrame
df["Date"] = pd.to_datetime(df["Date"])

# Get the minimum and maximum dates from the DataFrame
min_date = df["Date"].min()
max_date = df["Date"].max()




col1, col2 = st.columns(2)
df["Date"] = pd.to_datetime(df["Date"])

# Get the minimum and maximum dates from the DataFrame
min_date = df["Date"].min()
max_date = df["Date"].max()

# Set default values for date input widgets
default_start_date = min_date.date()
default_end_date = max_date.date()

# Display the date input widgets in two columns
with col1:
        date1 = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=default_end_date)
with col2:
        # Set the minimum value of the end date input dynamically based on the selected start date
        min_end_date = min(date1, default_end_date)
        date2 = st.date_input("End Date", min_value=min_end_date, max_value=max_date.date(), value=default_end_date)

    # Convert start_date and end_date to Timestamp objects
date1 = pd.Timestamp(date1)
date2 = pd.Timestamp(date2)

    # Apply date filtering to the DataFrame
filtered_df = df[(df["Date"] >= date1) & (df["Date"] <= date2)].copy()
    # date filtering section ends here



    # date filtering section ends here


    # Define initial options for the selectboxes
all_factories = ["All"] + list(filtered_df["Factory"].unique())
all_mill_nos = ["All"] + list(filtered_df["Mill No."].unique())
all_buyers = ["All"] + list(filtered_df["Buyer's Name"].unique())
all_cont_nos = ["All"] + list(filtered_df["Cont. No"].unique())

    # Create a column for filtering data
col1, col2, col3, col4 = st.columns(4)

    # Create selectboxes for filtering
with col1:
        selected_factory = st.selectbox("Factory", all_factories)

    # Dynamically update options for Mill No. based on selected factory
if selected_factory != "All":
        factories_df = filtered_df[filtered_df["Factory"] == selected_factory]
        all_mill_nos = ["All"] + list(factories_df["Mill No."].unique())
else:
        all_mill_nos = ["All"] + list(filtered_df["Mill No."].unique())

with col2:
        selected_mill_no = st.selectbox("Mill No.", all_mill_nos)

    # Dynamically update options for Buyer's Name based on selected factory and mill
if selected_mill_no != "All" and selected_factory != "All":
        mill_df = filtered_df[(filtered_df["Mill No."] == selected_mill_no) & (filtered_df["Factory"] == selected_factory)]
        all_buyers = ["All"] + list(mill_df["Buyer's Name"].unique())
elif selected_factory != "All":
        factories_df = filtered_df[filtered_df["Factory"] == selected_factory]
        all_buyers = ["All"] + list(factories_df["Buyer's Name"].unique())
else:
        all_buyers = ["All"] + list(filtered_df["Buyer's Name"].unique())

with col3:
        selected_buyer = st.selectbox("Buyer's Name", all_buyers)

    # Dynamically update options for Cont. No based on selected filters
if selected_mill_no != "All" and selected_factory != "All" and selected_buyer != "All":
        contact_df = filtered_df[(filtered_df["Mill No."] == selected_mill_no) & (filtered_df["Factory"] == selected_factory) & (filtered_df["Buyer's Name"] == selected_buyer)]
        all_cont_nos = ["All"] + list(contact_df["Cont. No"].unique())
elif selected_mill_no != "All" and selected_factory != "All":
        contact_df = filtered_df[(filtered_df["Mill No."] == selected_mill_no) & (filtered_df["Factory"] == selected_factory)]
        all_cont_nos = ["All"] + list(contact_df["Cont. No"].unique())
elif selected_factory != "All":
        contact_df = filtered_df[filtered_df["Factory"] == selected_factory]
        all_cont_nos = ["All"] + list(contact_df["Cont. No"].unique())

elif selected_buyer != "All":
        contact_df = filtered_df[filtered_df["Buyer's Name"] == selected_buyer]
        all_cont_nos = ["All"] + list(contact_df["Cont. No"].unique())
else:
        all_cont_nos = ["All"] + list(filtered_df["Cont. No"].unique())

with col4:
        selected_cont_no = st.selectbox("Cont. No", all_cont_nos)

st.markdown("")
st.markdown("")

    # Filter the data based on selected filters
filtered_df = filtered_df.copy()
if selected_factory != "All":
        filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]
if selected_mill_no != "All":
        filtered_df = filtered_df[filtered_df["Mill No."] == selected_mill_no]
if selected_buyer != "All":
        filtered_df = filtered_df[filtered_df["Buyer's Name"] == selected_buyer]
if selected_cont_no != "All":
        filtered_df = filtered_df[filtered_df["Cont. No"] == selected_cont_no]



    # Define the function to generate a download link for Excel
def get_table_download_link(df, filename):
        excel_file_buffer = BytesIO()
        df.to_excel(excel_file_buffer, index=False)
        excel_file_buffer.seek(0)
        b64 = base64.b64encode(excel_file_buffer.read()).decode()
        href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">Download file</a>'
        return href


if selected_factory=="All":
        factory_df_selected=filtered_df
        with st.expander("View DataFrame"):
            # Display the DataFrame within the expander
            st.write(factory_df_selected)

            # Generate a download button for the DataFrame
else:
        factory_df_selected=filtered_df
        selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

        # Filter the DataFrame based on the selected factories
        factory_df_selected = factory_df_selected[factory_df_selected['Factory'].isin(selected_factory)]
        

        with st.expander("View DataFrame"):
            # Display the DataFrame within the expander
            st.write(factory_df_selected)
            # Generate a download button for the DataFrame
            

st.markdown(get_table_download_link(factory_df_selected, "Production Details"), unsafe_allow_html=True)

st.markdown("")



col1,col2,col3=st.columns(3)
bagsize_vs_prodbale = factory_df_selected.groupby(factory_df_selected["Bag Size"], as_index=False)["Daily Packing Production Bales"].sum()
bagsize_vs_despatchedbale = factory_df_selected.groupby(factory_df_selected["Bag Size"], as_index=False)["Despatched Bales"].sum()
bagsize_vs_closingbale = factory_df_selected.groupby(factory_df_selected["Bag Size"], as_index=False)["Closing Stock Bales"].sum()


with col1:
     # Filter out rows with no values
    bagsize_vs_prodbale_filtered = bagsize_vs_prodbale[bagsize_vs_prodbale["Daily Packing Production Bales"] > 0]

    # Create a bar chart for production by factory
    fig = px.bar(bagsize_vs_prodbale_filtered, x="Bag Size", y="Daily Packing Production Bales", 
                text=['{:,.2f}'.format(x) for x in bagsize_vs_prodbale_filtered["Daily Packing Production Bales"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=["#488A99"] * len(bagsize_vs_prodbale_filtered))
    fig.update_layout(title="Production: Bag Size vs Bale")
                    
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Filter out rows with no values
    bagsize_vs_despatchedbale_filtered = bagsize_vs_despatchedbale[bagsize_vs_despatchedbale["Despatched Bales"] > 0]

    # Create a bar chart for production by factory
    fig = px.bar(bagsize_vs_despatchedbale_filtered, x="Bag Size", y="Despatched Bales", 
                text=['{:,.2f}'.format(x) for x in bagsize_vs_despatchedbale_filtered["Despatched Bales"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=["#488A99"] * len(bagsize_vs_despatchedbale_filtered))
    fig.update_layout(title="Despatch: Bag Size vs Bale")
                    
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                    
    st.plotly_chart(fig, use_container_width=True)
with col3:
    # Filter out rows with no values
    bagsize_vs_closingbale_filtered = bagsize_vs_closingbale[bagsize_vs_closingbale["Closing Stock Bales"] > 0]

    # Create a bar chart for production by factory
    fig = px.bar(bagsize_vs_closingbale_filtered, x="Bag Size", y="Closing Stock Bales", 
                text=['{:,.2f}'.format(x) for x in bagsize_vs_closingbale_filtered["Closing Stock Bales"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=["#488A99"] * len(bagsize_vs_closingbale_filtered))
    fig.update_layout(title="Closing: Bag Size vs Bale")
                    
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                    
    st.plotly_chart(fig, use_container_width=True)



col1,col2,col3=st.columns(3)
bagsize_vs_prodtons = factory_df_selected.groupby(factory_df_selected["Bag Size"], as_index=False)["Daily Packing Production Tons"].sum()
bagsize_vs_despatchedtons = factory_df_selected.groupby(factory_df_selected["Bag Size"], as_index=False)["Despatched Tons"].sum()
bagsize_vs_closingtons = factory_df_selected.groupby(factory_df_selected["Bag Size"], as_index=False)["Despatched Tons"].sum()


with col1:
     # Filter out rows with no values
    bagsize_vs_prodtons_filtered = bagsize_vs_prodtons[bagsize_vs_prodtons["Daily Packing Production Tons"] > 0]

    # Create a bar chart for production by factory
    fig = px.bar(bagsize_vs_prodtons_filtered, x="Bag Size", y="Daily Packing Production Tons", 
                text=['{:,.2f}'.format(x) for x in bagsize_vs_prodtons_filtered["Daily Packing Production Tons"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=["#488A99"] * len(bagsize_vs_prodtons_filtered))
    fig.update_layout(title="Production: Bag Size vs Tons")
                    
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Filter out rows with no values
    bagsize_vs_despatchedtons_filtered = bagsize_vs_despatchedtons[bagsize_vs_despatchedtons["Despatched Tons"] > 0]

    # Create a bar chart for production by factory
    fig = px.bar(bagsize_vs_despatchedtons_filtered, x="Bag Size", y="Despatched Tons", 
                text=['{:,.2f}'.format(x) for x in bagsize_vs_despatchedtons_filtered["Despatched Tons"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=["#488A99"] * len(bagsize_vs_despatchedtons_filtered))
    fig.update_layout(title="Despatch: Bag Size vs Tons")
                    
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                    
    st.plotly_chart(fig, use_container_width=True)
with col3:
    # Filter out rows with no values
    bagsize_vs_closingtons_filtered = bagsize_vs_closingtons[bagsize_vs_closingtons["Despatched Tons"] > 0]

    # Create a bar chart for production by factory
    fig = px.bar(bagsize_vs_closingtons_filtered, x="Bag Size", y="Despatched Tons", 
                text=['{:,.2f}'.format(x) for x in bagsize_vs_closingtons_filtered["Despatched Tons"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=["#488A99"] * len(bagsize_vs_closingtons_filtered))
    fig.update_layout(title="Closing: Bag Size vs Tons")
                    
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                    
    st.plotly_chart(fig, use_container_width=True)