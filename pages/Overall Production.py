import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Production Dashboard!!", page_icon=":bar_chart:", layout="wide")


st.title(" :bar_chart: Production Dashboard ")
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


# date filtering starts here
col1, col2=st.columns((2))
df["date"]=pd.to_datetime(df["date"])

# getting the min and max date
startdate=pd.to_datetime(df["date"]).min()
enddate=pd.to_datetime(df["date"]).max()


with col1:
    date1=pd.to_datetime(st.date_input("Start Date",startdate))

with col2:
    date2=pd.to_datetime(st.date_input("End Date", enddate))

df=df[(df["date"]>=date1) & (df["date"]<=date2)].copy()

# date filtering section ends here



st.sidebar.header("Choose your filter: ")
# Create for Factory Name
factory=st.sidebar.multiselect("Pick Location",
                               df["Factory"].unique(),
                               default=df["Factory"].unique()
                               )

if not factory:
    df2=df.copy()
else:
    df2=df[df["Factory"].isin(factory)]


# Create for mill no
millno=st.sidebar.multiselect("Choose Mill No.",
                              df["Mill No."].unique(),
                              default=df["Mill No."].unique()
                              )

if not millno:
    df3=df2.copy()
else:
    df3=df2[df2["Mill No."].isin(millno)]


# Create for product type
quality=st.sidebar.multiselect("Select quality"
                               ,df["Product Type"].unique()
                               ,default=df["Product Type"].unique()
                               )

if not quality:
    df4=df3.copy()
else:
    df4=df3[df3["Product Type"].isin(quality)]

# sidebar for filtering data ends here




# # Filter the data based on quality, product type and mill no
if not factory and not millno and not quality:
    filtered_df = df
elif not factory and not millno:
    filtered_df = df[df["Product Type"].isin(quality)]
elif not quality and not factory:
    filtered_df = df[df["Mill No."].isin(millno)]
elif millno and quality:
    filtered_df = df3[df["Mill No."].isin(millno) & df3["Product Type"].isin(quality)]
elif quality and factory:
    filtered_df = df3[df["Product Type"].isin(quality) & df3["Factory"].isin(factory)]
elif factory and millno:
    filtered_df = df3[df["Factory"].isin(factory) & df3["Mill No."].isin(millno)]
elif quality:
    filtered_df = df3[df3["Product Type"].isin(quality)]
elif millno:
    filtered_df = df3[df3["Mill No."].isin(millno)]


elif factory:
    filtered_df = df3[df3["Factory"].isin(factory)]
  
else:
    filtered_df = df3[df3["Product Type"].isin(quality) & df3["Mill No."].isin(millno) & df3["Factory"].isin(factory)]

# data filtering ends here


# time series analysis data



# Extract day from the date column
filtered_df["day"] = filtered_df["date"].dt.day

# Group by day and sum the actual production for each day
linechart = filtered_df.groupby("day")["actual production"].sum().reset_index()

# Plot the line chart
fig2 = px.line(linechart, x="day", y="actual production", labels={"Production": "Ton"}, height=500, width=1000, template="gridon",title="Time Series Analysis")

# Display the line chart using Streamlit
st.plotly_chart(fig2, use_container_width=True)

# Optional: Provide a button to download the data
with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')