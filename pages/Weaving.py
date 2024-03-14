import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import base64
from io import BytesIO



warnings.filterwarnings("ignore")


st.set_page_config(page_title="Weaving", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Weaving")
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
        
jute_issue_df=pd.read_excel("Weaving_prod_format.xlsx",skiprows=5)

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
grade = ["All"] + list(df["Shift"].unique())

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
    grade = ["All"] + list(mill_df["Shift"].unique())
elif selected_factory != "All":
    factories_df = df[df["Factory"] == selected_factory]
    grade = ["All"] + list(factories_df["Shift"].unique())
else:
    grade = ["All"] + list(df["Shift"].unique())

with col3:
    selected_grade = st.selectbox("Shift", grade)


# Filter the data based on selected filters
filtered_df = df.copy()
if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]
if selected_mill_no != "All":
    filtered_df = filtered_df[filtered_df["Mill No."] == selected_mill_no]
if selected_grade != "All":
    filtered_df = filtered_df[filtered_df["Shift"] == selected_grade]





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




col1,col2,col3=st.columns(3)



       




       


# jute_issue=factory_df["Issue"].sum()/1000
# accuracy_qty=(factory_df["Demand"].sum()/1000)+(factory_df["Shortage"].sum()/1000)
# accuracy_rate = ((factory_df["Demand"].sum() / 1000) + (factory_df["Shortage"].sum() / 1000)) / (factory_df["Demand"].sum() / 1000)
# accuracy_rate_percentage = accuracy_rate * 100

# access=factory_df["Access"].sum()/1000
# shortage=factory_df["Shortage"].sum()/1000

# formatted_requisition="{:.2f}".format(product)
# formatted_issue="{:.2f}".format(jute_issue)
# formatted_accuracy_qty="{:.2f}".format(accuracy_qty)
# formatted_access_qty="{:.2f}".format(access)
# formatted_shortage_qty="{:.2f}".format(abs(shortage))
# formatted_accuracy_rate="{:.2f}%".format(accuracy_rate_percentage)





# with col1:

#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Product</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             sacking,hessian,soil,normal=st.columns(4)
            
#             with sacking:
#                 original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Sacking</p>'
            
#                 st.markdown(original_title,unsafe_allow_html=True)
#                 value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{sacking_value}</p>'
#                 st.markdown(value,unsafe_allow_html=True)

#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
            

#             with hessian:
#                 original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Hessian</p>'
            
#                 st.markdown(original_title,unsafe_allow_html=True)
#                 value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{hessian_value}</p>'
#                 st.markdown(value,unsafe_allow_html=True)

#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
            
#             with soil:
#                 original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Soil</p>'
            
#                 st.markdown(original_title,unsafe_allow_html=True)
#                 value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{soil_value}</p>'
#                 st.markdown(value,unsafe_allow_html=True)

#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
            

#             with normal:
#                 original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Normal</p>'
            
#                 st.markdown(original_title,unsafe_allow_html=True)
#                 value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{normal_value}</p>'
#                 st.markdown(value,unsafe_allow_html=True)

#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
        
        

col1,col2=st.columns(2)

factory_df=filtered_df
products=factory_df["Product"].unique()
sacking_value = 0
hessian_value = 0
soil_value = 0
normal_value = 0
for product in products:
    looms_sum = factory_df[factory_df["Product"] == product]["No. of Looms"].sum()
    if product == "SACKING":
        sacking_value = looms_sum
    elif product in ["F. B. HESSIAN", "N. HESSIAN"]:
        hessian_value += looms_sum
    elif product == "SOIL SAVER":
        soil_value = looms_sum
    else:
        normal_value += looms_sum

with col1:
   # Define the product categories and their corresponding values
    product_categories = ['Sacking', 'Hessian', 'Soil', 'Normal']
    product_values = [sacking_value, hessian_value, soil_value, normal_value]
    text_values = [value for value in product_values]

    # Define color palette list (replace with desired colors)
    color_palette = ['royalblue', 'firebrick', 'gold', 'seagreen']

    # Create a DataFrame from the product categories and values
    product_df = pd.DataFrame({'Product': product_categories, 'Value': product_values})

    # Create a bar chart using Plotly Express
    fig = px.bar(product_df, x='Product', y='Value',
                # Use 'Value' as the color code for individual bars
                
                labels={'Value': 'Value', 'Product': 'Product Category'},
                title='Product Values by Category',
                template='seaborn')

    # Add custom styling to the bar chart
    fig.update_layout(font=dict(family='Arial', size=15, color='Black'),
                    xaxis=dict(tickmode='array', tickvals=product_categories, title='Product Category'),
                    yaxis=dict(title='Value'),
                    barmode='group',
                    width=1000, height=500,  # Adjust width and height here
                    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins as needed
                    bargap=0.1)  # Adjust the gap between bars here

    # Set the text to display on the bars
    fig.update_traces(text=text_values, textposition='outside',
                    textfont=dict(size=15, color='Black', family='Arial'))

    # Display the bar chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
                        







with col2:
    prod_sacking_value=0
    prod_hessian_value = 0
    prod_soil_value = 0
    prod_normal_value = 0
    for product in products:
        looms_sum = factory_df[factory_df["Product"] == product]["Oz/Yd."].sum()
        if product == "SACKING":
            prod_sacking_value = looms_sum
        elif product in ["F. B. HESSIAN", "N. HESSIAN"]:
            prod_hessian_value += looms_sum
        elif product == "SOIL SAVER":
            prod_soil_value = looms_sum
        else:
            prod_normal_value += looms_sum

    # Define the product categories and their corresponding values
    product_categories = ['Sacking', 'Hessian', 'Soil', 'Normal']
    product_values = [prod_sacking_value, prod_hessian_value, prod_soil_value, prod_normal_value]
    text_values = ["{:.2f}".format(value) for value in product_values]

    # Define color palette list (replace with desired colors)
    color_palette = ['royalblue', 'firebrick', 'gold', 'seagreen']

    # Create a DataFrame from the product categories and values
    product_df = pd.DataFrame({'Product': product_categories, 'Value': product_values})

    # Create a bar chart using Plotly Express
    fig = px.bar(product_df, x='Product', y='Value',
                labels={'Value': 'Value', 'Product': 'Product Category'},
                title='Product Values by Category',
                template='seaborn')

    # Add custom styling to the bar chart
    fig.update_layout(font=dict(family='Arial', size=15, color='Black'),
                    xaxis=dict(tickmode='array', tickvals=product_categories, title='Product Category'),
                    yaxis=dict(title='Value'),
                    barmode='group',
                    width=1000, height=500,  # Adjust width and height here
                    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins as needed
                    bargap=0.1)  # Adjust the gap between bars here

    # Set the text to display on the bars
    fig.update_traces(text=text_values, textposition='outside',
                    textfont=dict(size=15, color='Black', family='Arial'))

    # Display the bar chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)





col1,col2,col3=st.columns(3)


with col1:

    cut_sacking_value=0
    cut_hessian_value = 0
    cut_soil_value = 0
    cut_normal_value = 0
    for product in products:
        looms_sum = factory_df[factory_df["Product"] == product]["Actual Production Cuts"].sum()
        if product == "SACKING":
            cut_sacking_value = looms_sum
        elif product in ["F. B. HESSIAN", "N. HESSIAN"]:
            cut_hessian_value += looms_sum
        elif product == "SOIL SAVER":
            cut_soil_value = looms_sum
        else:
            cut_normal_value += looms_sum
   # Define the product categories and their corresponding values
    product_categories = ['Sacking', 'Hessian', 'Soil', 'Normal']
    product_values = [cut_sacking_value, cut_hessian_value, cut_soil_value, cut_normal_value]
    text_values = ["{:.2f}".format(value) for value in product_values]

    # Define color palette list (replace with desired colors)
    color_palette = ['royalblue', 'firebrick', 'gold', 'seagreen']

    # Create a DataFrame from the product categories and values
    product_df = pd.DataFrame({'Product': product_categories, 'Value': product_values})

    # Create a bar chart using Plotly Express
    fig = px.bar(product_df, x='Product', y='Value',
                # Use 'Value' as the color code for individual bars
                
                labels={'Value': 'Value', 'Product': 'Product Category'},
                title='Product Values by Category',
                template='seaborn')

    # Add custom styling to the bar chart
    fig.update_layout(font=dict(family='Arial', size=15, color='Black'),
                    xaxis=dict(tickmode='array', tickvals=product_categories, title='Product Category'),
                    yaxis=dict(title='Value'),
                    barmode='group',
                    width=1000, height=500,  # Adjust width and height here
                    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins as needed
                    bargap=0.1)  # Adjust the gap between bars here

    # Set the text to display on the bars
    fig.update_traces(text=text_values, textposition='outside',
                    textfont=dict(size=15, color='Black', family='Arial'))

    # Display the bar chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
                        







with col2:
    prod_sacking_value=0
    prod_hessian_value = 0
    prod_soil_value = 0
    prod_normal_value = 0
    for product in products:
        looms_sum = factory_df[factory_df["Product"] == product]["Actual Production Tons"].sum()
        if product == "SACKING":
            prod_sacking_value = looms_sum
        elif product in ["F. B. HESSIAN", "N. HESSIAN"]:
            prod_hessian_value += looms_sum
        elif product == "SOIL SAVER":
            prod_soil_value = looms_sum
        else:
            prod_normal_value += looms_sum

    # Define the product categories and their corresponding values
    product_categories = ['Sacking', 'Hessian', 'Soil', 'Normal']
    product_values = [prod_sacking_value, prod_hessian_value, prod_soil_value, prod_normal_value]
    text_values = ["{:.2f}".format(value) for value in product_values]

    # Define color palette list (replace with desired colors)
    color_palette = ['royalblue', 'firebrick', 'gold', 'seagreen']

    # Create a DataFrame from the product categories and values
    product_df = pd.DataFrame({'Product': product_categories, 'Value': product_values})

    # Create a bar chart using Plotly Express
    fig = px.bar(product_df, x='Product', y='Value',
                labels={'Value': 'Value', 'Product': 'Product Category'},
                title='Product Values by Category',
                template='seaborn')

    # Add custom styling to the bar chart
    fig.update_layout(font=dict(family='Arial', size=15, color='Black'),
                    xaxis=dict(tickmode='array', tickvals=product_categories, title='Product Category'),
                    yaxis=dict(title='Value'),
                    barmode='group',
                    width=1000, height=500,  # Adjust width and height here
                    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins as needed
                    bargap=0.1)  # Adjust the gap between bars here

    # Set the text to display on the bars
    fig.update_traces(text=text_values, textposition='outside',
                    textfont=dict(size=15, color='Black', family='Arial'))

    # Display the bar chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)


with col3:
    # Define the list of selected departments
    selected_hessian = ["F. B. HESSIAN", "N. HESSIAN"]
    selected_sacking = ["SACKING"]
    selected_normal = ["NORMAL"]
    selected_soil_saver = ["SOIL SAVER"]

    # Filter the DataFrame to include only the selected departments
    selected_df_hessian = filtered_df[filtered_df["Product"].isin(selected_hessian)]
    selected_df_sacking = filtered_df[filtered_df["Product"].isin(selected_sacking)]
    selected_df_normal = filtered_df[filtered_df["Product"].isin(selected_normal)]
    selected_df_soil_saver = filtered_df[filtered_df["Product"].isin(selected_soil_saver)]

    # Calculate mean efficiency for each product category
    hessian_efficiency = selected_df_hessian["Efficiency"].mean()
    sacking_efficiency = selected_df_sacking["Efficiency"].mean()
    normal_efficiency = selected_df_normal["Efficiency"].mean()
    soil_saver_efficiency = selected_df_soil_saver["Efficiency"].mean()

    # Create a DataFrame to hold the aggregated data
    aggregated_df = pd.DataFrame({
        "Product": ["Hessian", "Sacking", "Normal", "Soil Saver"],
        "Efficiency": [hessian_efficiency, sacking_efficiency, normal_efficiency, soil_saver_efficiency]
    })

    # Create a bar chart using Plotly Express
    fig = px.bar(aggregated_df, x='Product', y='Efficiency',
                labels={'Efficiency': 'Mean Efficiency', 'Product': 'Product Category'},
                title='Mean Efficiency by Product Category',
                template='seaborn')

    # Add custom styling to the bar chart
    fig.update_layout(font=dict(family='Arial', size=15, color='Black'),
                    xaxis=dict(title='Product Category'),
                    yaxis=dict(title='Mean Efficiency'),
                    width=800, height=500,  # Adjust width and height here
                    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins as needed
                    bargap=0.1)  # Adjust the gap between bars here

    # Set the text to display on the bars in percentage format
    fig.update_traces(texttemplate='%{y:.2%}', textposition='outside',
                    textfont=dict(size=15, color='Black', family='Arial'))

    # Display the bar chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)