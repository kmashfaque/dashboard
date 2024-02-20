import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import plotly.graph_objs as go


warnings.filterwarnings("ignore")

st.set_page_config(page_title="Over All Production!!", page_icon=":bar_chart:", layout="wide")


st.title(" :bar_chart: Production Details Dashboard")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)


# file uploading section
# fl=st.file_uploader(":file_folder: Upload a file", type=(["csv","xlsx","txt","xls"]))
# if fl is not None:
#     filename=fl.name
#     st.write(filename)
#     df=pd.read_excel(filename,sheet_name="Daily Production")
#     hands_df=pd.read_excel(filename)
# else:
#     os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
#     df=pd.read_excel("production.xlsx")
#     hands_df=pd.read_excel("HandsPerTon.xlsx")

os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
    
df=pd.read_excel("production.xlsx",sheet_name="Overall Production")

unique_date=df["Date"]



# # date filtering starts here
col1, col2=st.columns((2))
df["Date"]=pd.to_datetime(df["Date"])

# Get the minimum and maximum dates from the DataFrame
min_date = df["Date"].min()
max_date = df["Date"].max()

# Set default values for date input widgets
default_start_date = min_date.date()
default_end_date = max_date.date()

# Display the date input widgets in two columns
col1, col2 = st.columns(2)

with col1:
    date1 = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=default_end_date)

with col2:
    date2 = st.date_input("End Date", min_value=min_date.date(), max_value=max_date.date(), value=default_end_date)

# Convert start_date and end_date to Timestamp objects
date1 = pd.Timestamp(date1)
date2 = pd.Timestamp(date2)

df=df[(df["Date"]>=date1) & (df["Date"]<=date2)].copy()

# date filtering section ends here



# Define initial options for the selectboxes
all_factories = ["All"] + list(df["Factory"].unique())
all_mill_nos = ["All"] + list(df["Mill No."].unique())
all_buyers = ["All"] + list(df["Buyer's Name"].unique())
all_cont_nos = ["All"] + list(df["Contact No."].unique())

# Create a column for filtering data
col1, col2, col3, col4 = st.columns(4)

# Create selectboxes for filtering
with col1:
    selected_factory = st.selectbox("Factory", all_factories)

# Dynamically update options for Mill No. based on selected factory
if selected_factory != "All":
    factories_df = df[df["Factory"] == selected_factory]
    all_mill_nos = ["All"] + list(factories_df["Mill No."].unique())
else:
    all_mill_nos = ["All"] + list(df["Mill No."].unique())

with col2:
    selected_mill_no = st.selectbox("Mill No.", all_mill_nos)

# Dynamically update options for Buyer's Name based on selected factory and mill
if selected_mill_no != "All" and selected_factory != "All":
    mill_df = df[(df["Mill No."] == selected_mill_no) & (df["Factory"] == selected_factory)]
    all_buyers = ["All"] + list(mill_df["Buyer's Name"].unique())
elif selected_factory != "All":
    factories_df = df[df["Factory"] == selected_factory]
    all_buyers = ["All"] + list(factories_df["Buyer's Name"].unique())
else:
    all_buyers = ["All"] + list(df["Buyer's Name"].unique())

with col3:
    selected_buyer = st.selectbox("Buyer's Name", all_buyers)

# Dynamically update options for Contact No. based on selected filters
if selected_mill_no != "All" and selected_factory != "All" and selected_buyer != "All":
    contact_df = df[(df["Mill No."] == selected_mill_no) & (df["Factory"] == selected_factory) & (df["Buyer's Name"] == selected_buyer)]
    all_cont_nos = ["All"] + list(contact_df["Contact No."].unique())
elif selected_mill_no != "All" and selected_factory != "All":
    contact_df = df[(df["Mill No."] == selected_mill_no) & (df["Factory"] == selected_factory)]
    all_cont_nos = ["All"] + list(contact_df["Contact No."].unique())
elif selected_factory != "All":
    contact_df = df[df["Factory"] == selected_factory]
    all_cont_nos = ["All"] + list(contact_df["Contact No."].unique())
else:
    all_cont_nos = ["All"] + list(df["Contact No."].unique())

with col4:
    selected_cont_no = st.selectbox("Contact No.", all_cont_nos)

st.markdown("")
st.markdown("")

# Filter the data based on selected filters
filtered_df = df.copy()
if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]
if selected_mill_no != "All":
    filtered_df = filtered_df[filtered_df["Mill No."] == selected_mill_no]
if selected_buyer != "All":
    filtered_df = filtered_df[filtered_df["Buyer's Name"] == selected_buyer]
if selected_cont_no != "All":
    filtered_df = filtered_df[filtered_df["Contact No."] == selected_cont_no]




col1,col2,col3,col4,col5=st.columns(5)



factory_df=filtered_df

production=factory_df["actual production"].sum()
efficiency=factory_df["Efficiency"].mean()
converted_production=factory_df["Converted Production"].sum()
total_frame=factory_df["Frame"].sum()

formatted_actual_production="{:.2f}".format(production)
formatted_efficiency="{:.0%}".format(efficiency)
formatted_converted_production="{:.2f}".format(converted_production)

with col1:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Production</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_actual_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    

with col2:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Efficiency</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    


with col3:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Converted Production</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_converted_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    
with col4:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Frame</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{total_frame}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")





# Start sections for charts
col1, col2, col3 = st.columns((3))

# Display factory-wise charts
if selected_factory=="All":
    factory_df = filtered_df.groupby(filtered_df["Factory"], as_index=False)["actual production"].sum()
    efficiency_df = filtered_df.groupby(filtered_df["Factory"], as_index=False)["Efficiency"].mean()
    
   
    with col1:
        try:
            # Create a bar chart for production by factory
            fig = px.bar(factory_df, x="Factory", y="actual production", text=['{:,.2f}'.format(x) for x in factory_df["actual production"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(factory_df))
            fig.update_layout(title="Production ")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        try:
            # Create a bar chart for efficiency by factory
            fig = px.bar(efficiency_df, x="Factory", y="Efficiency", text=['{:,.2f}'.format(x) for x in efficiency_df["Efficiency"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #1C4E80"] * len(efficiency_df))
            fig.update_layout(title="Efficiency ")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")
    

    with col3:

        quality_df = filtered_df.groupby(filtered_df["Product Type"], as_index=False)["actual production"].sum()
    
        try:
                # Create a bar chart for production by factory
                fig = px.bar(quality_df, x="Product Type", y="actual production", text=['{:,.2f}'.format(x) for x in quality_df["actual production"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(quality_df))
                fig.update_layout(title="Quality vs Production")
                st.plotly_chart(fig, use_container_width=True)

        except IndexError:
                    st.warning("No data found for the specified filter.")
            


# Display mill-wise data if a factory is selected
else:

    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from the selected factory DataFrame
    selected_mills_production = factory_df_selected["Mill No."].unique()

    # Filter the DataFrame to include only the selected mills
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    
   
    
    mill_production_df = mill_df.groupby(["Mill No."], as_index=False)["actual production"].sum()
    mill_efficiency_df = mill_df.groupby(["Mill No."], as_index=False)["Efficiency"].mean()

  


    with col1:
        try:
            # Create a bar chart for production by mill number
            fig = px.bar(mill_production_df, x="Mill No.", y="actual production",
                         text=['{:,.2f}'.format(x) for x in mill_production_df["actual production"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #488A99"] * len(mill_production_df))
            fig.update_layout(title="Production")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        try:
            # Create a bar chart for efficiency by mill number
            fig = px.bar(mill_efficiency_df, x="Mill No.", y="Efficiency",
                         text=['{:,.2f}'.format(x) for x in mill_efficiency_df["Efficiency"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #1C4E80"] * len(mill_efficiency_df))
            fig.update_layout(title="Efficiency ")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col3:
        quality_df = filtered_df.groupby(filtered_df["Product Type"], as_index=False)["actual production"].sum()
    
        try:
                # Create a bar chart for production by factory
                fig = px.bar(quality_df, x="Product Type", y="actual production", text=['{:,.2f}'.format(x) for x in quality_df["actual production"]],
                template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(quality_df))
                fig.update_layout(title="Quality vs Production")
                st.plotly_chart(fig, use_container_width=True)

        except IndexError:
                    st.warning("No data found for the specified filter.")

        

col1,col2=st.columns([3,2])    




count_df = filtered_df.groupby(filtered_df["count"], as_index=False)["actual production"].sum()
ply_df=filtered_df.groupby(filtered_df["Ply"],as_index=False)["actual production"].sum()


with col1:
      
    try:
            # Create a bar chart for production by factory
            fig = px.bar(count_df, x="count", y="actual production", text=['{:,.2f}'.format(x) for x in count_df["actual production"]],
            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
            fig.update_layout(title="Countwise Production")
            st.plotly_chart(fig, use_container_width=True)

    except IndexError:
                st.warning("No data found for the specified filter.")


with col2:
    try:
                # Create a bar chart for production by factory
                fig = px.bar(ply_df, x="Ply", y="actual production", text=['{:,.2f}'.format(x) for x in ply_df["actual production"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(ply_df))
                fig.update_layout(title="Ply")
                st.plotly_chart(fig, use_container_width=True)

    except IndexError:
                st.warning("No data found for the specified filter.")


# frame vs count chart


count_df = filtered_df.groupby(filtered_df["count"], as_index=False)["Frame"].sum()
col1,col2=st.columns(2)

with col1:
      
    try:
            # Create a bar chart for production by factory
            fig = px.bar(count_df, x="count", y="Frame", text=['{:,.2f}'.format(x) for x in count_df["Frame"]],
            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
            fig.update_layout(title="Frame vs Count")
            st.plotly_chart(fig, use_container_width=True)

    except IndexError:
                st.warning("No data found for the specified filter.")

# count vs efficiency

count_df = filtered_df.groupby(filtered_df["count"], as_index=False)["Efficiency"].mean()

with col2:
         
    try:
            # Create a bar chart for production by factory
            fig = px.bar(count_df, x="count", y="Efficiency", text=['{:,.2f}'.format(x) for x in count_df["Efficiency"]],
            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
            fig.update_layout(title="Efficiency vs Count")
            st.plotly_chart(fig, use_container_width=True)

    except IndexError:
                st.warning("No data found for the specified filter.")

        



# frame with count vs production 
        
# if selected_factory == "All":
#     count_df = df.groupby(df["count"], as_index=False)["actual production"].sum()
    
#     try:
#         # Create a bar chart for production by factory
#         fig = px.bar(count_df, x="count", y="actual production", 
#                      text=['{:,.2f}'.format(x) for x in count_df["actual production"]],
#                      template="seaborn", width=1000, height=500, 
#                      color_discrete_sequence=[" #488A99"] * len(count_df))
#         fig.update_layout(title="Countwise Production")
        
#         # Add scatter plot for frame data
#         frame_data = df.groupby("count", as_index=False)["Frame"].sum()
#         fig.add_trace(go.Scatter(x=frame_data["count"], y=frame_data["Frame"], 
#                                  mode="markers", name="Frame Data", marker=dict(color="red", size=10)))

#         # Add frame data as text annotations
#         for i, row in frame_data.iterrows():
#             fig.add_annotation(x=row["count"], y=row["Frame"], text=f'{row["Frame"]:.2f}',
#                                font=dict(color='white', size=12), showarrow=True, arrowhead=1)

#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#         st.warning("No data found for the specified filter.")

# # Display mill-wise data if a factory is selected
# else:
#     selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

#     # Filter the DataFrame based on the selected factories
#     factory_df_selected = df[df['Factory'].isin(selected_factory)]

#     # Extract unique mill numbers from the selected factory DataFrame
#     selected_mills_production = factory_df_selected["Mill No."].unique()

#     # Filter the DataFrame to include only the selected mills
#     mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]

#     if selected_mill_number == "All":
#         mill_count_df = mill_df.groupby(["count"], as_index=False)["actual production"].sum()
#     else:
#         # Group by both mill number to get production data for ply
#         selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
#         mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
#         selected_mills = mill_df_selected["count"].unique()
#         mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
#         mill_count_df = mill_df_count.groupby(["count"], as_index=False)["actual production"].sum()

#     try:
#         # Create a bar chart for production by mill number
#         fig = px.bar(mill_count_df, x="count", y="actual production",
#                      text=['{:,.2f}'.format(x) for x in mill_count_df["actual production"]],
#                      template="seaborn", width=1000, height=500,
#                      color_discrete_sequence=[" #488A99"] * len(mill_count_df))
#         fig.update_layout(title="Countwise Production")

#         # Add scatter plot for frame data
#         frame_data = mill_df.groupby("count", as_index=False)["Frame"].sum()
#         fig.add_trace(go.Scatter(x=frame_data["count"], y=frame_data["Frame"],
#                                  mode="markers", name="Frame Data", marker=dict(color="red", size=10)))

#         # Add frame data as text annotations
#         for i, row in frame_data.iterrows():
#             fig.add_annotation(x=row["count"], y=row["Frame"], text=f'{row["Frame"]:.2f}',
#                                font=dict(color='white', size=12), showarrow=True, arrowhead=1)

#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#         st.warning("No data found for the specified filter.")
















