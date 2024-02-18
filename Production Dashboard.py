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
    
df=pd.read_excel("production.xlsx")
hands_df=pd.read_excel("HandsPerTon.xlsx")
stock_df=pd.read_excel("Stocks.xlsx")

unique_date=df["Date"].unique()
hands_df=hands_df[hands_df["Date"].isin(unique_date)]
stock_df=stock_df[stock_df["Date"].isin(unique_date)]


# # date filtering starts here
# col1, col2=st.columns((2))
# df["Date"]=pd.to_datetime(df["Date"])

# # getting the min and max date
# startdate=pd.to_datetime(df["Date"]).min()
# enddate=pd.to_datetime(df["Date"]).max()


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


# sidebar for filtering data starts here

# st.sidebar.header("Choose your filter: ")
# # Create for Factory Name
# factory=st.sidebar.multiselect("Pick Location",
#                                df["Factory"].unique(),
#                                default=df["Factory"].unique()
#                                )

# if selected_factory == "All":
#     filtered_df = df.copy()
#     hands_df_all=han
# else:
#     filtered_df = df[df["Factory"] == selected_factory]

# if selected_factory == "All":
#     hands_df = hands_df.copy()
# else:
#     hands_df = hands_df[hands_df["Factory"] == selected_factory]



# Create for mill no
# millno=st.sidebar.multiselect("Choose Mill",
#                               df["Mill No."].unique(),
#                               default=df["Mill No."].unique()
#                               )

# if not millno:
#     df3=df2.copy()
# else:
#     df3=df2[df2["Mill No."].isin(millno)]


# Create for product type
# quality=st.sidebar.multiselect("Select Quality"
#                                ,df["Product Type"].unique()
#                                ,default=df["Product Type"].unique()
#                                )

# if not quality:
#     df4=df3.copy()
# else:
#     df4=df3[df3["Product Type"].isin(quality)]

# sidebar for filtering data ends here




# # Filter the data based on quality, product type and mill no
# if not factory and not millno and not quality:
#     filtered_df = df
# elif not factory and not millno:
#     filtered_df = df[df["Product Type"].isin(quality)]
# elif not quality and not factory:
#     filtered_df = df[df["Mill No."].isin(millno)]
# elif millno and quality:
#     filtered_df = df3[df["Mill No."].isin(millno) & df3["Product Type"].isin(quality)]
# elif quality and factory:
#     filtered_df = df3[df["Product Type"].isin(quality) & df3["Factory"].isin(factory)]
# elif factory and millno:
#     filtered_df = df3[df["Factory"].isin(factory) & df3["Mill No."].isin(millno)]
# elif quality:
#     filtered_df = df3[df3["Product Type"].isin(quality)]
# elif millno:
#     filtered_df = df3[df3["Mill No."].isin(millno)]
# elif factory:
#     filtered_df = df3[df3["Factory"].isin(factory)]
# else:
#     filtered_df = df3[df3["Product Type"].isin(quality) & df3["Mill No."].isin(millno) & df3["Factory"].isin(factory)]

# data filtering ends here


# section for hands per ton
# if not factory and not millno and not quality:
#     filtered_df_1 = hands_df
# elif factory and millno:
#     filtered_df_1 = hands_df[hands_df["Factory"].isin(factory) & hands_df["Mill No."].isin(millno)]
# elif millno:
#     filtered_df_1 = hands_df[hands_df["Mill No."].isin(millno)]
# elif factory:
#     filtered_df_1 = hands_df[hands_df["Factory"].isin(factory)]
# elif quality:
#     filtered_df_1 = hands_df
# else:
#     filtered_df_1 = hands_df["Mill No."].isin(millno) & hands_df["Factory"].isin(factory) 

# hands per ton section ends here


# # Stock Filter the data based on product type and mill no
# if not factory and not millno and not quality:
#     filtered_df_stock= stock_df
# elif factory and millno:
#     filtered_df_stock = stock_df[stock_df["Factory"].isin(factory) & stock_df["Mill No."].isin(millno)]
# elif millno:
#     filtered_df_stock = stock_df[stock_df["Mill No."].isin(millno)]
# elif factory:
#     filtered_df_stock = stock_df[stock_df["Factory"].isin(factory)]
# elif quality:
#     filtered_df_stock = stock_df  
# else:
#     filtered_df_stock = stock_df["Mill No."].isin(millno) & stock_df["Factory"].isin(factory) 

# Stock data filtering ends here



# section for text columns
# actual_production=factory_df["actual production"].sum()

# efficiency=factory_df["Efficiency"].mean()

# converted_production=factory_df["Converted Production"].sum()

# total_frame=factory_df["frame"].sum()

# total_hands=hands_df["Hands"].sum()


# stock_despatch=stock_df["Despatch M/Ton"].sum()


# if not factory and not millno and not quality:

#     with col1:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Production</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_actual_production}</p>'
#         # st.markdown(value,unsafe_allow_html=True)
#         # st.markdown("")
#         # st.markdown("")
#         # st.markdown("")


#         col1_target, col1_actual =st.columns((2))
#         with col1_target:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Target</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
#             st.markdown(value,unsafe_allow_html=True)

#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
            
#         with col1_actual:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Actual</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
#             st.markdown(value,unsafe_allow_html=True)

#             st.markdown("")
#             st.markdown("")
#             st.markdown("")

#     with col2:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Efficiency</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_efficiency}</p>'
#         st.markdown(value,unsafe_allow_html=True)
#         st.markdown("")
#         st.markdown("")
#         st.markdown("")

#     with col3:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Converted Production</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_converted_production}</p>'
#         st.markdown(value,unsafe_allow_html=True)
#         st.markdown("")
#         st.markdown("")
#         st.markdown("")
        

#     with col4:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Total Frame</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{total_frame}</p>'
#         # st.markdown(value,unsafe_allow_html=True)
#         # st.markdown("")
#         # st.markdown("")
#         # st.markdown("")

#         existing, running =st.columns((2))
#         with existing:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Existing</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
#             st.markdown(value,unsafe_allow_html=True)

            
#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
#         with running:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Running</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
#             st.markdown(value,unsafe_allow_html=True)

#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
        
        
#         with col5:
           
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Total Hands</p>'
#             st.markdown(original_title,unsafe_allow_html=True)
#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_total_hands}</p>'
#             st.markdown(value,unsafe_allow_html=True)
#             st.markdown("")
#             st.markdown("")
#             st.markdown("")


#         with col6:
           
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
#             st.markdown(original_title,unsafe_allow_html=True)
#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_stock_despatch}</p>'
#             st.markdown(value,unsafe_allow_html=True)
#             st.markdown("")
#             st.markdown("")
#             st.markdown("")

# else:
#     with col1:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Production</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_actual_production}</p>'
#         # st.markdown(value,unsafe_allow_html=True)
#         # st.markdown("")
#         # st.markdown("")
#         # st.markdown("")


#         col1_target, col1_actual =st.columns((2))
#         with col1_target:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Target</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
#             st.markdown(value,unsafe_allow_html=True)

#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
            
#         with col1_actual:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Actual</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
#             st.markdown(value,unsafe_allow_html=True)

#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
            

#     with col2:


#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Efficiency</p>'
        
#         st.markdown(original_title,unsafe_allow_html=True)
#         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
#         st.markdown(value,unsafe_allow_html=True)

#         st.markdown("")
#         st.markdown("")
#         st.markdown("")
       
    

#     with col3:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Converted Production</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_converted_production}</p>'
#         st.markdown(value,unsafe_allow_html=True)
#         st.markdown("")
#         st.markdown("")
#         st.markdown("")
   
#     with col4:
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Total Frame</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{total_frame}</p>'
#         # st.markdown(value,unsafe_allow_html=True)
#         # st.markdown("")
#         # st.markdown("")
#         # st.markdown("")

#         existing, running =st.columns((2))
#         with existing:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Existing</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
#             st.markdown(value,unsafe_allow_html=True)

            
#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
#         with running:
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Running</p>'
#             st.markdown(original_title,unsafe_allow_html=True)

#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{total_frame}</p>'
#             st.markdown(value,unsafe_allow_html=True)

#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
#     with col5:
            
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Total Hands</p>'
#             st.markdown(original_title,unsafe_allow_html=True)
#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_total_hands}</p>'
#             st.markdown(value,unsafe_allow_html=True)
#             st.markdown("")
#             st.markdown("")
#             st.markdown("")

    
#     with col6:
           
#             original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
#             st.markdown(original_title,unsafe_allow_html=True)
#             value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_stock_despatch}</p>'
#             st.markdown(value,unsafe_allow_html=True)
#             st.markdown("")
#             st.markdown("")
#             st.markdown("")
    




# filter data based on factory

col1,col2,col3,col4,col5,col6=st.columns((6))



if selected_factory=="All":


    factory_df=df
    hands_df_all=hands_df
    stock_all=stock_df
    actual_production=factory_df["actual production"].sum()
    efficiency=factory_df["Efficiency"].mean()
    converted_production=factory_df["Converted Production"].sum()
    total_frame=factory_df["frame"].sum()
    total_hands=hands_df["Hands"].sum()
    stock_despatch=stock_df["Despatch M/Ton"].sum()

    formatted_actual_production="{:.2f}".format(actual_production)
    formatted_efficiency="{:.0%}".format(efficiency)
    formatted_converted_production="{:.2f}".format(converted_production)
    formatted_total_hands="{:.2f}".format(total_hands)
    formatted_stock_despatch="{:.2f}".format(stock_despatch)

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
        
        
        with col5:
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Total Hands</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_total_hands}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")


        with col6:
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_stock_despatch}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")

else:


    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    hands_df_selected = hands_df[hands_df["Factory"].isin(selected_factory)]
    stock_df_selected = stock_df[stock_df["Factory"].isin(selected_factory)]
    actual_production=factory_df_selected["actual production"].sum()
    efficiency=factory_df_selected["Efficiency"].mean()
    converted_production=factory_df_selected["Converted Production"].sum()
    total_frame=factory_df_selected["frame"].sum()
    total_hands=hands_df_selected["Hands"].sum()
    stock_despatch=stock_df_selected["Despatch M/Ton"].sum()


    formatted_actual_production="{:.2f}".format(actual_production)
    formatted_efficiency="{:.0%}".format(efficiency)
    formatted_converted_production="{:.2f}".format(converted_production)
    formatted_total_hands="{:.2f}".format(total_hands)
    formatted_stock_despatch="{:.2f}".format(stock_despatch)
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
    with col5:
            
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Total Hands</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_total_hands}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")

    
    with col6:
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_stock_despatch}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")
    

    
                




# end sections for text columns



# # groupby section for data visualization
# factory_df=filtered_df.groupby(filtered_df["Factory"], as_index=False)["actual production"].sum()
# countwise_df=filtered_df.groupby(filtered_df["count"], as_index=False)["actual production"].sum()
# buyer_df=filtered_df.groupby(filtered_df["Buyer's Name"], as_index=False)["actual production"].sum()

# factory_df_efficiency=filtered_df.groupby(filtered_df["Factory"], as_index=False)["Efficiency"].mean()

# # starts sections for charts
# col1,col2,col3=st.columns((3))
# with col1:
#     # Set a custom color scheme
#     # original_title = '<p style="font-family:Ssns-Serif; color:Black; font-size: 18px; font-weight:bold;">Factory wise Actual Production</p>'
#     # st.markdown(original_title,unsafe_allow_html=True)

#     try:
#     # Create the bar chart with custom color
#         fig=px.bar(factory_df,x="Factory",y="actual production",text=['{:,.2f}'.format(x) for x in factory_df["actual production"]],
#         template = "seaborn",width=350,height=350, color_discrete_sequence=[" #488A99"]*len(factory_df))

#         # Update layout
#         fig.update_layout(title="Production")

#     except IndexError:
#     # Handle the case when the filter doesn't find any data
#         st.warning("No data found for the specified filter.")

#     # Display the bar chart if no error occurred
#     if 'fig' in locals():
#         st.plotly_chart(fig,use_container_width=True)

# with col2:

#     try:
#         JJMLN=["JJMLN"]
#         JJMLF=[ "JJMLF"]
#         SJIL=["SJIL"]
#         # selected_mils_2B=["Mill No. 2B"]


#         # Filter the DataFrame to include only the selected departments
#         selected_df_1 = filtered_df[filtered_df["Factory"].isin(JJMLN)]

#         # Group by "Section" (department) and sum the values of "Hands" for each department
#         JJMLN = selected_df_1["Efficiency"].mean()


#         # Filter the DataFrame to include only the selected departments
#         selected_df_2 = filtered_df[filtered_df["Factory"].isin(JJMLF)]

#         # Group by "Section" (department) and sum the values of "Hands" for each department
#         JJMLF = selected_df_2["Efficiency"].mean()


#         # Filter the DataFrame to include only the selected departments
#         selected_df_3 = filtered_df[filtered_df["Factory"].isin(SJIL)]

#         # Group by "Section" (department) and sum the values of "Hands" for each department
#         SJIL = selected_df_3["Efficiency"].mean()


#         # # Filter the DataFrame to include only the selected departments
#         # selected_df_4 = filtered_df[filtered_df["Factory"].isin(selected_mils_2B)]

#         # # Group by "Section" (department) and sum the values of "Hands" for each department
#         # mill2B = selected_df_4["Efficiency"].mean()


#         # Create a DataFrame to concatenate the sums
#         combined_df = pd.DataFrame({
#         "Factory": ["JJMLN"] + ["JJMLF"] + ["SJIL"] ,
#         "Efficiency": [JJMLN] + [JJMLF] + [SJIL] 
# })

#         # Create a pie chart for the combined data
#         # fig_combined = px.pie(combined_df, values="Efficiency", names="Mill No.", hole=0.5)
#         fig=px.bar(combined_df,x="Factory",y="Efficiency",text=['{:,.2f}'.format(x) for x in combined_df["Efficiency"]],
#                 template = "seaborn",width=350,height=350, color_discrete_sequence=[" #AC3E31"]*len(combined_df))

#         # Update layout
#         fig.update_layout(title="Efficiency")

       

#     except IndexError:
#         # Handle the case when the filter doesn't find any data
#         st.warning("No data found for the specified filter.")

#     if 'fig' in locals():
#         st.plotly_chart(fig,use_container_width=True)




# # factory_df_hands_per_ton=filtered_df_1.groupby(filtered_df_1["Mill No."], as_index=False)["Hands Per Ton"].sum()
# factory_df_hands_per_ton_1=filtered_df_1.groupby(filtered_df_1["Factory"], as_index=False)["Hands Per Ton"].sum()
# with col3:
#     try:
            
#         # original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Factory wise Hands Per Ton</p>'
#         # st.markdown(original_title,unsafe_allow_html=True)
#         fig = px.bar(factory_df_hands_per_ton_1, x="Factory",y="Hands Per Ton",text=['{:,.2f}'.format(x) for x in factory_df_hands_per_ton_1["Hands Per Ton"]],
#                     template="seaborn",height=350,width=350,color_discrete_sequence=["#1C4E80"] * len(factory_df_hands_per_ton_1))
#         fig.update_layout(title="Hands Per Ton")
#         st.plotly_chart(fig,use_container_width=True)

    
#     except IndexError:
#         st.warning("No data found for the specified filter.")



# original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;text-align:center;">Count wise production</p>'
# st.markdown(original_title,unsafe_allow_html=True)
# try:
#     # Create the bar chart with custom color
#     fig2 = px.bar(countwise_df, x="count", y="actual production", text=['{:,.2f}'.format(x) for x in countwise_df["actual production"]],
#                   height=500, width=1000, color_discrete_sequence=["#488A99"] * len(countwise_df))
# except IndexError:
#     # Handle the case when the filter doesn't find any data
#     st.warning("No data found for the specified filter.")

# # Display the bar chart if no error occurred
# if 'fig2' in locals():
#     st.plotly_chart(fig2, use_container_width=True, height=500)


# with st.expander("View Data of Count:"):
#     st.write(countwise_df.T.style.background_gradient(cmap="Blues"))
#     # csv = countwise_df.to_csv(index=False).encode("utf-8")
#     # st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv", mime ='text/csv')



# original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;text-align:center;">Buyer wise production</p>'
# st.markdown(original_title,unsafe_allow_html=True)
# try:
#     # Create the bar chart with custom color
#     fig2 = px.bar(buyer_df, x="Buyer's Name", y="actual production", text=['{:,.2f}'.format(x) for x in buyer_df["actual production"]],
#                   height=500, width=1000, color_discrete_sequence=["#488A99"] * len(buyer_df))
# except IndexError:
#     # Handle the case when the filter doesn't find any data
#     st.warning("No data found for the specified filter.")

# # Display the bar chart if no error occurred
# if 'fig2' in locals():
#     st.plotly_chart(fig2, use_container_width=True, height=500)



# with st.expander("View Data of Count:"):
#     st.write(buyer_df.T.style.background_gradient(cmap="Blues"))
#     # csv = countwise_df.to_csv(index=False).encode("utf-8")
#     # st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv", mime ='text/csv')





# Groupby section for data visualization
# if selected_factory =="All":
#     factory_df = df.groupby(df["Factory"], as_index=False)["actual production"].sum()
#     efficiency_df = df.groupby(df["Factory"], as_index=False)["Efficiency"].mean()
#     hands_per_ton_df = hands_df.groupby(hands_df["Factory"], as_index=False)["Hands Per Ton"].sum()
# else:
#     factory_df = df.groupby(df["Mill No."], as_index=False)["actual production"].sum()
#     efficiency_df = df.groupby(df["Mill No."], as_index=False)["Efficiency"].mean()
#     hands_per_ton_df = hands_df.groupby(hands_df["Mill No."], as_index=False)["Hands Per Ton"].sum()


# Start sections for charts
col1, col2, col3 = st.columns((3))

# Display factory-wise charts
if selected_factory=="All":
    factory_df = df.groupby(df["Factory"], as_index=False)["actual production"].sum()
    efficiency_df = df.groupby(df["Factory"], as_index=False)["Efficiency"].mean()
    hands_per_ton_df = hands_df.groupby(hands_df["Factory"], as_index=False)["Hands Per Ton"].sum()
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
            fig = px.bar(efficiency_df, x="Factory", y="Efficiency", text=['{:,.2f}'.format(x) for x in efficiency_df["Efficiency"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #1C4E80"] * len(efficiency_df))
            fig.update_layout(title="Efficiency by Factory")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col3:
        try:
            # Create a bar chart for hands per ton by factory
            fig = px.bar(hands_per_ton_df, x="Factory", y="Hands Per Ton", text=['{:,.2f}'.format(x) for x in hands_per_ton_df["Hands Per Ton"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=["#AC3E31"] * len(hands_per_ton_df))
            fig.update_layout(title="Hands Per Ton by Factory")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

# Display mill-wise data if a factory is selected
else:

    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    hands_df_selected = hands_df[hands_df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from both DataFrames
    selected_mills_production = factory_df_selected["Mill No."].unique()
    selected_mills_hands = hands_df_selected["Mill No."].unique()

    # Combine the mill numbers from both DataFrames
    selected_mills = set(selected_mills_production).intersection(selected_mills_hands)

    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    hands_mill_no = hands_df_selected[hands_df_selected["Mill No."].isin(selected_mills_hands)]
    mill_production_df = mill_df.groupby(["Mill No."], as_index=False)["actual production"].sum()
    mill_efficiency_df = mill_df.groupby(["Mill No."], as_index=False)["Efficiency"].mean()
    mill_hands_per_ton_df = hands_mill_no.groupby(["Mill No."], as_index=False)["Hands Per Ton"].sum()

  

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
            fig = px.bar(mill_efficiency_df, x="Mill No.", y="Efficiency",
                         text=['{:,.2f}'.format(x) for x in mill_efficiency_df["Efficiency"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #1C4E80"] * len(mill_efficiency_df))
            fig.update_layout(title="Efficiency by Mill Number")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col3:
        try:
            # Create a bar chart for hands per ton by mill number
            fig = px.bar(mill_hands_per_ton_df, x="Mill No.", y="Hands Per Ton",
                         text=['{:,.2f}'.format(x) for x in mill_hands_per_ton_df["Hands Per Ton"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=["#AC3E31"] * len(mill_hands_per_ton_df))
            fig.update_layout(title="Hands Per Ton by Mill Number")
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
    hands_df_selected = hands_df[hands_df['Factory'].isin(selected_factory)]

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

   



# selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory
# factory_df_selected = df[df['Factory'].isin(selected_factory)]
# countwise_df=factory_df_selected.groupby(df["count"],as_index=False)["actual production"]




# original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;text-align:center;">Count wise actual production</p>'
# st.markdown(original_title,unsafe_allow_html=True)


# try:
#     # Create the bar chart with custom color
#     fig2 = px.bar(countwise_df, x="count", y="actual production", text=['{:,.2f}'.format(x) for x in countwise_df["actual production"]],
#                   height=500, width=1000, color_discrete_sequence=["#488A99"] * len(countwise_df))
# except IndexError:
#     # Handle the case when the filter doesn't find any data
#     st.warning("No data found for the specified filter.")

# # Display the bar chart if no error occurred
# if 'fig2' in locals():
#     st.plotly_chart(fig2, use_container_width=True, height=500)



# with st.expander("View Data of Count:"):
#     st.write(countwise_df.T.style.background_gradient(cmap="Blues"))
    # csv = countwise_df.to_csv(index=False).encode("utf-8")
    # st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv", mime ='text/csv')