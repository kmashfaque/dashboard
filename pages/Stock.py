import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
import base64
from io import BytesIO

warnings.filterwarnings("ignore")


st.set_page_config(page_title="Overall Stock", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Stock Details")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)


# Load your data
df = pd.read_excel("Stocks.xlsx")


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
    date1 = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=default_start_date)

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
    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = filtered_df[filtered_df['Factory'].isin(selected_factory)]
    

    with st.expander("View DataFrame"):
        # Display the DataFrame within the expander
        st.write(factory_df_selected)
        # Generate a download button for the DataFrame
        

st.markdown(get_table_download_link(factory_df_selected, "Production Details"), unsafe_allow_html=True)

st.markdown("")




# section for data vlaue

production_value=filtered_df["Production M/Ton"].sum()
formatted_production_value="{:.2f}".format(production_value)


despatch_value=filtered_df["Despatch M/Ton"].sum()
formatted_despatch_value="{:.2f}".format(despatch_value)

filtered_date_closing_df=filtered_df[filtered_df["Date"]==date2]
closing_stock=filtered_date_closing_df["Closing Stock M/Ton"].sum()
formatted_closing_stock="{:.2f}".format(closing_stock)


loose_stock=filtered_date_closing_df["Loose Stock"].sum()
formatted_loose_stock="{:.2f}".format(loose_stock)


filtered_date_1_date_df=filtered_df[filtered_df["Date"]==date1]
opening_value=filtered_date_1_date_df["Opening Stock M/Ton"].sum()
formatted_opening_value="{:.2f}".format(opening_value)

col1,col2,col3,col4,col5=st.columns(5)

with col1:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center;">{formatted_production_value}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")


      
with col2:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center;">{formatted_despatch_value}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

with col3:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Closing Stock</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center;">{formatted_closing_stock}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        

with col4:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;text-align:center">Loose Stock</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center;text-align:center">{formatted_loose_stock}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")


with col5:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;text-align:center">Opening Stock</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center;text-align:center">{formatted_opening_value}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

# end section for value 


# section for chart
        
col1,col2,col3=st.columns(3)


start_date = filtered_df["Date"].min()
end_date = filtered_df["Date"].max()
date_diff = (end_date - start_date).days

if date_diff<=5:


    with col1:
        try:
            # Select only the columns of interest
            production_df = filtered_df[["Production Pallet", "Production Truss", "Production Carton"]]

            # Sum the production quantities across all counts
            total_production = production_df.sum()

            # Create a DataFrame for the total production
            total_production_df = pd.DataFrame(total_production).reset_index()

            # Rename the columns for plotting
            total_production_df.columns = ["Product", "Total Production"]

            # Plot the DataFrame as a stacked bar chart
            fig = px.bar(total_production_df, x="Product", y="Total Production",
                        template="seaborn", width=350,height=350,title=" Production",
                        color_discrete_sequence=["#488A99", "#1C4E80", "#7C77B9", "#FF5733"],
                        # Specify custom colors if needed
                        text="Total Production"
                        
                        )

            # Update the layout
            fig.update_layout(xaxis_title="Product",yaxis_title="Production")

            # Display the chart
            st.plotly_chart(fig, use_container_width=True)
        
        except:
            st.warning("No data found for the specified filter.")



    with col2:
        try:
            # Select only the columns of interest
            production_df = filtered_df[["Despatch Pallet", "Despatch Truss", "Despatch Carton"]]

            # Sum the production quantities across all counts
            total_production = production_df.sum()

            # Create a DataFrame for the total production
            total_production_df = pd.DataFrame(total_production).reset_index()

            # Rename the columns for plotting
            total_production_df.columns = ["Product", "Total Production"]

            # Plot the DataFrame as a stacked bar chart
            fig = px.bar(total_production_df, x="Product", y="Total Production",
                        template="seaborn", width=350,height=350,title="Despatch",
                        color_discrete_sequence=["#488A99", "#1C4E80", "#7C77B9", "#FF5733"],
                        # Specify custom colors if needed
                        text="Total Production"
                        
                        )

            # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Production", barmode="stack")

            # Display the chart
            st.plotly_chart(fig, use_container_width=True)
        
        except:
            st.warning("No data found for the specified filter.")


    with col3:
        try:
        
            countwise_despatch=filtered_df.groupby("Count",as_index=False)["Despatch M/Ton"].sum()

            # Filter out rows with zero values in "Despatch M/Ton"
            countwise_despatch = countwise_despatch[countwise_despatch["Despatch M/Ton"] > 0]

            # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_despatch, x="Count", y="Despatch M/Ton",
                        text=['{:,.2f}'.format(x) for x in countwise_despatch["Despatch M/Ton"]],
                        template="seaborn", width=350,height=350,title="Despatch (M/Ton)",
                        color_discrete_sequence=[" #488A99"] * len(countwise_despatch),
                        )

            # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Production", barmode="stack")

            # Display the chart
            st.plotly_chart(fig, use_container_width=True)

        except:
            st.warning("No data found for the specified filter.")


else:
    start_date = filtered_df["Date"].min()
    end_date = filtered_df["Date"].max()
    date_diff = (end_date - start_date).days

    try:


            # Group by "Count" and sum the "Production M/Ton" values
            countwise_production = filtered_df.groupby("Count", as_index=False)["Production M/Ton"].sum()

            
                # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_production, x="Count", y="Production M/Ton",
                            text=['{:,.2f}'.format(x) for x in countwise_production["Production M/Ton"]],
                            template="seaborn", width=800, height=500, title="Countwise Closing Stock",
                            color_discrete_sequence=[" #488A99"] * len(countwise_production))

                # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Production")

                # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    except:
            st.warning("No data found for the specified end date.")


    
    try:
        # Filter the DataFrame based on the end date
            filtered_df = df[df["Date"] == date1]

            # Group by "Count" and sum the "Loose Stock M/Ton" values
            countwise_loose_stock = filtered_df.groupby("Count", as_index=False)["Loose Stock"].sum()

            
                # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_loose_stock, x="Count", y="Loose Stock",
                            text=['{:,.2f}'.format(x) for x in countwise_loose_stock["Loose Stock"]],
                            template="seaborn", width=800, height=500, title="Countwise Opening Stock",
                            color_discrete_sequence=[" #488A99"] * len(countwise_loose_stock))

                # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Loose Stock")

                # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    except:
            st.warning("No data found for the specified end date.")



















col1,col2=st.columns(2)

if date_diff<=5:
     
    with col1:
        try:
        # Filter the DataFrame based on the end date
            filtered_df = df[df["Date"] == date2]

            # Group by "Count" and sum the "Closing Stock M/Ton" values
            countwise_closing_stock = filtered_df.groupby("Count", as_index=False)["Closing Stock M/Ton"].sum()

            
                # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_closing_stock, x="Count", y="Closing Stock M/Ton",
                            text=['{:,.2f}'.format(x) for x in countwise_closing_stock["Closing Stock M/Ton"]],
                            template="seaborn", width=800, height=500, title="Countwise Closing Stock",
                            color_discrete_sequence=[" #488A99"] * len(countwise_closing_stock))

                # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Closing Stock")

                # Display the chart
            st.plotly_chart(fig, use_container_width=True)
        except:
            st.warning("No data found for the specified end date.")


    with col2:
        try:
        # Filter the DataFrame based on the end date
            filtered_df = df[df["Date"] == date1]

            # Group by "Count" and sum the "Closing Stock M/Ton" values
            countwise_opeining_stock = filtered_df.groupby("Count", as_index=False)["Opening Stock M/Ton"].sum()

            
                # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_opeining_stock, x="Count", y="Opening Stock M/Ton",
                            text=['{:,.2f}'.format(x) for x in countwise_opeining_stock["Opening Stock M/Ton"]],
                            template="seaborn", width=800, height=500, title="Countwise Opening Stock",
                            color_discrete_sequence=[" #488A99"] * len(countwise_opeining_stock))

                # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Opening Stock")

                # Display the chart
            st.plotly_chart(fig, use_container_width=True)
        except:
            st.warning("No data found for the specified end date.")



else:
    
    try:
        # Filter the DataFrame based on the end date
            filtered_df = df[df["Date"] == date2]

            # Group by "Count" and sum the "Closing Stock M/Ton" values
            countwise_closing_stock = filtered_df.groupby("Count", as_index=False)["Closing Stock M/Ton"].sum()

            
                # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_closing_stock, x="Count", y="Closing Stock M/Ton",
                            text=['{:,.2f}'.format(x) for x in countwise_closing_stock["Closing Stock M/Ton"]],
                            template="seaborn", width=800, height=500, title="Countwise Closing Stock",
                            color_discrete_sequence=[" #488A99"] * len(countwise_closing_stock))

                # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Closing Stock")

                # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    except:
            st.warning("No data found for the specified end date.")


    
    try:
        # Filter the DataFrame based on the end date
            filtered_df = df[df["Date"] == date1]

            # Group by "Count" and sum the "Closing Stock M/Ton" values
            countwise_opeining_stock = filtered_df.groupby("Count", as_index=False)["Opening Stock M/Ton"].sum()

            
                # Plot the DataFrame as a stacked bar chart
            fig = px.bar(countwise_opeining_stock, x="Count", y="Opening Stock M/Ton",
                            text=['{:,.2f}'.format(x) for x in countwise_opeining_stock["Opening Stock M/Ton"]],
                            template="seaborn", width=800, height=500, title="Countwise Opening Stock",
                            color_discrete_sequence=[" #488A99"] * len(countwise_opeining_stock))

                # Update the layout
            fig.update_layout(xaxis_title="Product", yaxis_title="Opening Stock")

                # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    except:
            st.warning("No data found for the specified end date.")