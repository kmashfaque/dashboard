import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import base64
from io import BytesIO



warnings.filterwarnings("ignore")


st.set_page_config(page_title="Jute Issue", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Jute Issue")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)




# file uploading section
# fl=st.file_uploader(":file_folder: Upload a file", type=(["csv","xlsx","txt","xls"]))
# if fl is not None:
#     filename=fl.name
#     st.write(filename)
#     jute_issue_df=pd.read_excel(filename)
# else:
#     os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
        
#     jute_issue_df=pd.read_excel("HandsPerTon.xlsx")

os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
        
jute_issue_df=pd.read_excel("Juteissue - Copy.xlsx")

# date filtering starts here
col1, col2=st.columns((2))
jute_issue_df["Date"]=pd.to_datetime(jute_issue_df["Date"])

# Get the minimum and maximum dates from the DataFrame
min_date = jute_issue_df["Date"].min()
max_date = jute_issue_df["Date"].max()

# Set default values for date input widgets
default_start_date = min_date.date()
default_end_date = max_date.date()




col1, col2 = st.columns(2)
jute_issue_df["Date"] = pd.to_datetime(jute_issue_df["Date"])

# Get the minimum and maximum dates from the DataFrame
min_date = jute_issue_df["Date"].min()
max_date = jute_issue_df["Date"].max()

# Set default values for date input widgets
default_start_date = min_date.date()
default_end_date = max_date.date()

# Display the date input widgets in two columns
with col1:
    start_date = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=default_end_date)

with col2:
    # Set the minimum value of the end date input dynamically based on the selected start date
    min_end_date = min(start_date, default_end_date)
    end_date = st.date_input("End Date", min_value=min_end_date, max_value=max_date.date(), value=default_end_date)

# Convert start_date and end_date to Timestamp objects
start_date = pd.Timestamp(start_date)
end_date = pd.Timestamp(end_date)

# Apply date filtering to the DataFrame
df = jute_issue_df[(jute_issue_df["Date"] >= start_date) & (jute_issue_df["Date"] <= end_date)].copy()

# Define initial options for the selectboxes
all_factories = ["All"] + list(df["Factory"].unique())
all_mill_nos = ["All"] + list(df["Mill No."].unique())
grade = ["All"] + list(df["Jute Type"].unique())

# Create a column for filtering data
col1, col2, col3 = st.columns(3)

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

# Dynamically update options for Grade based on selected factory and mill
if selected_mill_no != "All" and selected_factory != "All":
    mill_df = df[(df["Mill No."] == selected_mill_no) & (df["Factory"] == selected_factory)]
    grade = ["All"] + list(mill_df["Jute Type"].unique())
elif selected_factory != "All":
    factories_df = df[df["Factory"] == selected_factory]
    grade = ["All"] + list(factories_df["Jute Type"].unique())
else:
    grade = ["All"] + list(df["Jute Type"].unique())

with col3:
    selected_grade = st.selectbox("Jute Type", grade)


# Filter the data based on selected filters
filtered_df = df.copy()
if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]
if selected_mill_no != "All":
    filtered_df = filtered_df[filtered_df["Mill No."] == selected_mill_no]
if selected_grade != "All":
    filtered_df = filtered_df[filtered_df["Jute Type"] == selected_grade]




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




col1,col2,col3,col4,col5,col6=st.columns(6)


factory_df=filtered_df
requisition=factory_df["Demand"].sum()/1000
jute_issue=factory_df["Issue"].sum()/1000
accuracy_qty=(factory_df["Demand"].sum()/1000)+(factory_df["Shortage"].sum()/1000)
accuracy_rate = ((factory_df["Demand"].sum() / 1000) + (factory_df["Shortage"].sum() / 1000)) / (factory_df["Demand"].sum() / 1000)
accuracy_rate_percentage = accuracy_rate * 100

access=factory_df["Access"].sum()/1000
shortage=factory_df["Shortage"].sum()/1000

formatted_requisition="{:.2f}".format(requisition)
formatted_issue="{:.2f}".format(jute_issue)
formatted_accuracy_qty="{:.2f}".format(accuracy_qty)
formatted_access_qty="{:.2f}".format(access)
formatted_shortage_qty="{:.2f}".format(abs(shortage))
formatted_accuracy_rate="{:.2f}%".format(accuracy_rate_percentage)



with col1:

            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Jute Requisition</p>'
            
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_requisition}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
        

with col2:


            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Jute Issued</p>'
            
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_issue}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
        


with col3:


            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Accuracy Quantity</p>'
            
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_accuracy_qty}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
        
with col4:


            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Accuracy Rate</p>'
            
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_accuracy_rate}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
with col5:


            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Access</p>'
            
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_access_qty}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")

with col6:


            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Shortage</p>'
            
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_shortage_qty}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")

# Start sections for charts
# col1 = st.columns((1))
# Display factory-wise charts

factory_df = ((filtered_df.groupby(filtered_df["Jute Type"])[["Demand","Issue"]].sum())/1000).reset_index()
# Filter out rows where both Demand and Issue are zero
factory_df = factory_df[(factory_df["Demand"] != 0) | (factory_df["Issue"] != 0)]

# Get the list of Grades with non-zero values
non_zero_grades = factory_df["Jute Type"].unique()

        
    
# with col1:
try:
        # Create a bar chart for production by factory
        fig = px.bar(factory_df, x="Jute Type", y=["Demand", "Issue"],
                         barmode='group', labels={"value": "Value", "variable": "Category"},
             title="Requisition and Issued by Jute Grade")
    
            
        fig.update_layout(title="Requisition and Issue Qty: Grade Wise ")
        st.plotly_chart(fig, use_container_width=True)
except IndexError:
                st.warning("No data found for the specified filter.")



  
# Assuming 'Issue' column contains numeric values represented as strings
filtered_df['Issue'] = pd.to_numeric(filtered_df['Issue'])

# Group by Grade and sum the Issue column, then divide the sum by 1000
grade_df = filtered_df.groupby(filtered_df["Jute Type"], as_index=False)["Issue"].sum()
grade_df["Issue"] /= 1000  # Divide the sum by 1000

# Filter out rows with zero values in the 'Issue' column
grade_df = grade_df[grade_df["Issue"] != 0]

try:
                # Create a bar chart for efficiency by factory
        fig = px.bar(grade_df, x="Jute Type", y="Issue", text=['{:,.2f}'.format(x) for x in grade_df["Issue"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #1C4E80"] * len(grade_df))
        fig.update_layout(title="Jute Issue: Grade Wise ")
        st.plotly_chart(fig, use_container_width=True)

except IndexError:
        st.warning("No data found for the specified filter.")
        

    # with col3:
    #         ply_df = filtered_df.groupby(filtered_df["Ply"], as_index=False)["achieved production"].sum()


    #         try:
    #                 # Create a bar chart for production by factory
    #                 fig = px.bar(ply_df, x="Ply", y="achieved production", text=['{:,.2f}'.format(x) for x in ply_df["achieved production"]],
    #                             template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(ply_df))
    #                 fig.update_layout(title="Production: Ply Wise")
    #                 st.plotly_chart(fig, use_container_width=True)

    #         except IndexError:
    #                 st.warning("No data found for the specified filter.")

            
                    








