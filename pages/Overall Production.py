



import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Production Dashboard!!", page_icon=":bar_chart:", layout="wide")


st.title(" :bar_chart: Production Dashboard")
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

# getting the min and max date
startdate=pd.to_datetime(df["Date"]).min()
enddate=pd.to_datetime(df["Date"]).max()


# with col1:
#     date1=pd.to_datetime(st.date_input("Start Date",startdate))

# with col2:
#     date2=pd.to_datetime(st.date_input("End Date", enddate))

# df=df[(df["Date"]>=date1) & (df["Date"]<=date2)].copy()

# date filtering section ends here




# Sidebar for filtering data
st.sidebar.header("Choose your filter:")
# Create for Factory Name
selected_factory = st.sidebar.selectbox("Pick Location",
                                        ["All"] + list(df["Factory"].unique()),
                                        index=0)


# filter data based on factory

col1,col2,col3,col4,col5,col6=st.columns((6))



if selected_factory=="All":


    factory_df=df
   
    actual_production=factory_df["actual production"].sum()
    efficiency=factory_df["Actual Efficiency"].mean()
    converted_production=factory_df["Converted Production"].sum()
    total_frame=factory_df["frame"].sum()
    
    formatted_actual_production="{:.2f}".format(actual_production)
    formatted_efficiency="{:.0%}".format(efficiency)
    formatted_converted_production="{:.2f}".format(converted_production)
   
    with col1:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_actual_production}</p>'
        # st.markdown(value,unsafe_allow_html=True)
        # st.markdown("")
        # st.markdown("")
        # st.markdown("")


        col1_target, col1_actual =st.columns((2))
        with col1_target:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Target</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
            
        with col1_actual:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Actual</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
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
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Total Frame</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{total_frame}</p>'
        # st.markdown(value,unsafe_allow_html=True)
        # st.markdown("")
        # st.markdown("")
        # st.markdown("")

        existing, running =st.columns((2))
        with existing:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Existing</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
            st.markdown(value,unsafe_allow_html=True)

            
            st.markdown("")
            st.markdown("")
            st.markdown("")
        with running:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Running</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
        
        
        

else:


    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    
    actual_production=factory_df_selected["actual production"].sum()
    efficiency=factory_df_selected["Actual Efficiency"].mean()
    converted_production=factory_df_selected["Converted Production"].sum()
    total_frame=factory_df_selected["frame"].sum()
 


    formatted_actual_production="{:.2f}".format(actual_production)
    formatted_efficiency="{:.0%}".format(efficiency)
    formatted_converted_production="{:.2f}".format(converted_production)
    
    with col1:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_actual_production}</p>'
        # st.markdown(value,unsafe_allow_html=True)
        # st.markdown("")
        # st.markdown("")
        # st.markdown("")


        col1_target, col1_actual =st.columns((2))
        with col1_target:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Target</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
            
        with col1_actual:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Actual</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
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
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Total Frame</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{total_frame}</p>'
        # st.markdown(value,unsafe_allow_html=True)
        # st.markdown("")
        # st.markdown("")
        # st.markdown("")

        existing, running =st.columns((2))
        with existing:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Existing</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
            st.markdown(value,unsafe_allow_html=True)

            
            st.markdown("")
            st.markdown("")
            st.markdown("")
        with running:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Running</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
   
    

    
            
# end sections for text columns



# Start sections for charts
col1, col2, col3 = st.columns((3))

# Display factory-wise charts
if selected_factory=="All":
    factory_df = df.groupby(df["Factory"], as_index=False)["actual production"].sum()
    efficiency_df = df.groupby(df["Factory"], as_index=False)["Actual Efficiency"].mean()
   
    with col1:
        try:
            # Create a bar chart for production by factory
            fig = px.bar(factory_df, x="Factory", y="actual production", text=['{:,.2f}'.format(x) for x in factory_df["actual production"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(factory_df))
            fig.update_layout(title="Production by Factory")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        try:
            # Create a bar chart for efficiency by factory
            fig = px.bar(efficiency_df, x="Factory", y="Actual Efficiency", text=['{:,.2f}'.format(x) for x in efficiency_df["Actual Efficiency"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #1C4E80"] * len(efficiency_df))
            fig.update_layout(title="Efficiency by Factory")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

   

# Display mill-wise data if a factory is selected
else:

    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    

    # Extract unique mill numbers from both DataFrames
    selected_mills_production = factory_df_selected["Mill No."].unique()
   
    
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    
    mill_production_df = mill_df.groupby(["Mill No."], as_index=False)["actual production"].sum()
    mill_efficiency_df = mill_df.groupby(["Mill No."], as_index=False)["Actual Efficiency"].mean()
  

  

    with col1:
        try:
            # Create a bar chart for production by mill number
            fig = px.bar(mill_production_df, x="Mill No.", y="actual production",
                         text=['{:,.2f}'.format(x) for x in mill_production_df["actual production"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #488A99"] * len(mill_production_df))
            fig.update_layout(title="Production by Mill Number")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        try:
            # Create a bar chart for efficiency by mill number
            fig = px.bar(mill_efficiency_df, x="Mill No.", y="Actual Efficiency",
                         text=['{:,.2f}'.format(x) for x in mill_efficiency_df["Actual Efficiency"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #1C4E80"] * len(mill_efficiency_df))
            fig.update_layout(title="Efficiency by Mill Number")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

   



# counwise production chart

if selected_factory=="All":
    count_df = df.groupby(df["count"], as_index=False)["actual production"].sum()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(count_df, x="count", y="actual production", text=['{:,.2f}'.format(x) for x in count_df["actual production"]],
        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
        fig.update_layout(title="Countwise Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
            st.warning("No data found for the specified filter.")

    

# Display mill-wise data if a factory is selected
else:

    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
   

    # Extract unique mill numbers from both DataFrames
    selected_mills_production = factory_df_selected["count"]
   


    mill_df = factory_df_selected[factory_df_selected["count"].isin(selected_mills_production)]
    mill_production_df = mill_df.groupby(["count"], as_index=False)["actual production"].sum()
    
  
    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_production_df, x="count", y="actual production",
        text=['{:,.2f}'.format(x) for x in mill_production_df["actual production"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_production_df))
        fig.update_layout(title="Countwise Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")

   


