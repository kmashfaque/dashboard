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
st.title(" :bar_chart: Weaving Production")
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


        
jute_issue_df=pd.read_excel("Weaving_prod.xlsx",skiprows=5)

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
shift = ["All"] + list(df["Shift"].unique())
grade = ["All"] + list(df["Product Type"].unique())

# Create a column for filtering data
col1, col2, col3,col4 = st.columns(4)

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

    # Dynamically update options for shift based on selected factory and mill
    if selected_mill_no != "All" and selected_factory != "All":
        mill_df = df[(df["Mill No."] == selected_mill_no) & (df["Factory"] == selected_factory)]
        shift = ["All"] + list(mill_df["Shift"].unique())
    elif selected_factory != "All":
        factories_df = df[df["Factory"] == selected_factory]
        shift = ["All"] + list(factories_df["Shift"].unique())
    else:
        shift = ["All"] + list(df["Shift"].unique())

with col3:
    selected_shift = st.selectbox("Shift", shift)
   # Dynamically update options for shift based on selected factory and mill
    if selected_mill_no != "All" and selected_factory != "All" and selected_shift!="All" and selected_product_type!="All":
        mill_df = df[(df["Mill No."] == selected_mill_no) & (df["Factory"] == selected_factory) & (df["Shift"]==selected_shift) ] 
        grade = ["All"] + list(mill_df["Product Type"].unique())
    elif selected_factory != "All":
        factories_df = df[df["Factory"] == selected_factory]
        grade = ["All"] + list(factories_df["Product Type"].unique())
    elif selected_mill_no != "All":
        factories_mill_no = df[df["Mill No."] == selected_mill_no]
        grade = ["All"] + list(factories_mill_no["Product Type"].unique())
    elif selected_mill_no != "All":
        shift = df[df["Shift"] == selected_mill_no]
        grade = ["All"] + list(shift["Product Type"].unique())
    else:
        grade = ["All"] + list(df["Product Type"].unique())


with col4:
    selected_product_type=st.selectbox("Product Type",grade)

   



# Filter the data based on selected filters
filtered_df = df.copy()
if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]
if selected_mill_no != "All":
    filtered_df = filtered_df[filtered_df["Mill No."] == selected_mill_no]
if selected_shift != "All":
    filtered_df = filtered_df[filtered_df["Shift"] == selected_shift]
if selected_product_type != "All":
    filtered_df = filtered_df[filtered_df["Product Type"] == selected_shift]



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




col1,col2,col3,col4=st.columns(4)



       


factory_df=factory_df_selected

loom_val=factory_df["No. of Looms"].sum()
production=factory_df["Actual Production Tons"].sum()
total_cut=factory_df["Actual Production Cuts"].sum()   
efficiency=factory_df["Efficiency"].mean()
formatted_actual_production="{:.2f}".format(production)
formatted_total_cut="{:.2f}".format(total_cut)
formatted_efficiency="{:.2f}".format(efficiency)




with col1:

        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">No of Looms</p>'
            
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{loom_val}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")

with col2:

        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Production</p>'
            
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{formatted_actual_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")           

with col3:

        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Total Cut</p>'
            
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{formatted_total_cut}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")   

with col4:

        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Efficiency</p>'
            
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")      
        
        
col1,col2=st.columns(2)
width_vs_prod = factory_df.groupby(factory_df["Width"], as_index=False)["Actual Production Tons"].sum()
width_vs_cuts = factory_df.groupby(factory_df["Width"], as_index=False)["Actual Production Cuts"].sum()


with col1:
     # Create a bar chart for production by factory
    fig = px.bar(width_vs_prod, x="Width", y="Actual Production Tons", text=['{:,.2f}'.format(x) for x in width_vs_prod["Actual Production Tons"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(width_vs_prod))
    fig.update_layout(title="Production: Width Wise")
                
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                
    st.plotly_chart(fig, use_container_width=True)


with col2:
     # Create a bar chart for production by factory
    fig = px.bar(width_vs_cuts, x="Width", y="Actual Production Cuts", text=['{:,.2f}'.format(x) for x in width_vs_cuts["Actual Production Cuts"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(width_vs_cuts))
    fig.update_layout(title="Cuts: Width Wise")
                
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                
    st.plotly_chart(fig, use_container_width=True)


col1,col2,col3=st.columns(3)


with col1:
    product_categories=factory_df.groupby(factory_df["Product Type"], as_index=False)["No. of Looms"].sum()

     # Create a bar chart for production by factory
    fig = px.bar(product_categories, x="Product Type", y="No. of Looms", text=['{:,.2f}'.format(x) for x in product_categories["No. of Looms"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(product_categories))
    fig.update_layout(title="Looms: Product Wise ")
                
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                
    st.plotly_chart(fig, use_container_width=True)
                        




with col2:

    product_categories=factory_df.groupby(factory_df["Product Type"], as_index=False)["Actual Production Tons"].sum()
    

    # Create a bar chart for production by factory
    fig = px.bar(product_categories, x="Product Type", y="Actual Production Tons", text=['{:,.2f}'.format(x) for x in product_categories["Actual Production Tons"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(product_categories))
    fig.update_layout(title="Production: Product Wise (M/Ton)")
                
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                
    st.plotly_chart(fig, use_container_width=True)



with col3:
    width_vs_loom = factory_df.groupby(factory_df["Width"], as_index=False)["No. of Looms"].sum()
    
    # Create a bar chart for production by factory
    fig = px.bar(width_vs_loom, x="Width", y="No. of Looms", text=['{:,.2f}'.format(x) for x in width_vs_loom["No. of Looms"]],
                            template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(width_vs_loom))
    fig.update_layout(title="Loom: Width Wise")
                
    # Convert the x-axis to categorical to remove blank spaces
    fig.update_xaxes(type='category')
                
    st.plotly_chart(fig, use_container_width=True)





    










