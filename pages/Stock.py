import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import plotly.graph_objs as go

warnings.filterwarnings("ignore")


st.set_page_config(page_title="Overall Stock", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Overall Stock")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)


os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
    
stock_df=pd.read_excel("Stocks.xlsx")


# sidebar for filtering data starts here
st.sidebar.header("Choose your filter: ")
# Create for Factory Name
factory=st.sidebar.multiselect("Pick Factory",
                               stock_df["Factory"].unique(),
                               default=stock_df["Factory"].unique()
                               )

if not factory:
    df2=stock_df.copy()
else:
    df2=stock_df[stock_df["Factory"].isin(factory)]


# Create for mill no
millno=st.sidebar.multiselect("Choose Mill No.",
                              stock_df["Mill No."].unique(),
                              default=stock_df["Mill No."].unique()
                              )

if not millno:
    df3=df2.copy()
else:
    df3=df2[df2["Mill No."].isin(millno)]




# date filtering starts here
col1, col2=st.columns((2))
stock_df["Date"]=pd.to_datetime(stock_df["Date"])

# getting the min and max date
startdate=pd.to_datetime(stock_df["Date"]).min()
enddate=pd.to_datetime(stock_df["Date"]).max()

with col1:
    date1=pd.to_datetime(st.date_input("Start Date",startdate))

with col2:
    date2=pd.to_datetime(st.date_input("End Date", enddate))

stock_df=stock_df[(stock_df["Date"]>=date1) & (stock_df["Date"]<=date2)].copy()

# date filtering section ends here



# # Filter the data based on quality, product type and mill no
if not factory and not millno:
    filtered_df = stock_df
elif factory and millno:
    filtered_df = df3[stock_df["Factory"].isin(factory) & df3["Mill No."].isin(millno)]
elif millno:
    filtered_df = df3[df3["Mill No."].isin(millno)]
elif factory:
    filtered_df = df3[df3["Factory"].isin(factory)]
else:
    df3["Mill No."].isin(millno) & df3["Factory"].isin(factory)

# data filtering ends here



# Dropdown for contact number
# col1, col2 = st.columns((1, 3))
# with col1:
options_for_contactId = ["Select"] + filtered_df["Cont. No"].unique().tolist()
search_criteria_cont_no = st.selectbox("Select you contact number: ", options_for_contactId)

# with col2:
if search_criteria_cont_no != "Select":
    # Filter the data based on the selected contact number
    filtered_df = filtered_df[filtered_df["Cont. No"] == search_criteria_cont_no]

#         # Dropdown for quality based on the filtered data
#         options_for_quality = filtered_df["Quality"].tolist()
#         search_criteria_quality = st.selectbox("Select your quality:", options_for_quality)
    

# data

# section for text columns
col1,col2,col3,col4,col5,col6,col7,col8=st.columns((8))
production_pallet=filtered_df["Production Pallet"].sum()
production_truss=filtered_df["Production Truss"].sum()
production_carton=filtered_df["Production Carton"].sum()
production_mton=filtered_df["Production M/Ton"].sum()
formatted_production_pallet="{:.2f}".format(production_pallet)
formatted_production_truss="{:.2f}".format(production_truss)
formatted_production_carton="{:.2f}".format(production_carton)
formatted_production_mton="{:.2f}".format(production_mton)




col1,col2,col3,col4=st.columns((4))

if not factory and not millno:

    with col1:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Pallet</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_pallet}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

    with col2:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Truss</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_truss}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

    with col3:
    # Set a custom color scheme
    # original_title = '<p style="font-family:Ssns-Serif; color:Black; font-size: 18px; font-weight:bold;">Factory wise Actual Production</p>'
    # st.markdown(original_title,unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Carton</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_carton}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        

    with col4:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_mton}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        

else:
    with col1:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Pallet</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_pallet}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

    with col2:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Truss</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_truss}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

    with col3:
    # Set a custom color scheme
    # original_title = '<p style="font-family:Ssns-Serif; color:Black; font-size: 18px; font-weight:bold;">Factory wise Actual Production</p>'
    # st.markdown(original_title,unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Carton</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_carton}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        

    with col4:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_mton}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        


# end sections for text columns
    



# col1, col2 = st.columns((1, 3))
# with col1:
#     options_for_contactId = ["Select"] + filtered_df["Cont. No"].unique().tolist()
#     search_criteria_cont_no = st.selectbox("Select your contact number: ", options_for_contactId)

# # Define filtered_by_contact_df outside of the if condition
# filtered_by_contact_df = filtered_df[filtered_df["Cont. No"] == search_criteria_cont_no]

# with col2:
#     if search_criteria_cont_no != "Select":
#         # Dropdown for quality based on the filtered data
#         options_for_quality = filtered_by_contact_df["Quality"].unique().tolist()
#         search_criteria_quality = st.selectbox("Select your quality:", options_for_quality)




# # Group by Factory and sum the production for each category
# grouped_df = filtered_df.groupby("Factory").agg({
#     "Production Pallet": "sum",
#     "Production Truss": "sum",
#     "Production Carton": "sum",
#     "Production M/Ton": "sum"
# }).reset_index()

# # Define the data for each bar chart
# data = [
#     go.Bar(x=grouped_df["Factory"], y=grouped_df["Production Pallet"], name="Production Pallet"),
#     go.Bar(x=grouped_df["Factory"], y=grouped_df["Production Truss"], name="Production Truss"),
#     go.Bar(x=grouped_df["Factory"], y=grouped_df["Production Carton"], name="Production Carton"),
#     go.Bar(x=grouped_df["Factory"], y=grouped_df["Production M/Ton"], name="Production M/Ton")
# ]

# # Define the layout
# layout = go.Layout(title="Production by Category",
#                    xaxis=dict(title="Factory"),
#                    yaxis=dict(title="Production"),
#                    barmode="group")

# # Create the figure
# fig = go.Figure(data=data, layout=layout)

# # Display the chart in Streamlit
# st.plotly_chart(fig)