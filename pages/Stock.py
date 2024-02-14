import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult

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



# dropdown for contact number
col1,col2=st.columns(2)

with col1:
    options_for_contactId=filtered_df["Cont. No"].tolist()

    search_criteria_cont_no=st.selectbox("Select you contact number: ",options_for_contactId)



with col2:
    # Filter the data based on the selected contact number
    filtered_df = filtered_df[filtered_df["Cont. No"] == search_criteria_cont_no]

    # Dropdown for quality based on the filtered data
    options_for_quality = filtered_df["Quality"].tolist()
    search_criteria_quality = st.selectbox("Select your quality:", options_for_quality)

# end dropdown section here
    


