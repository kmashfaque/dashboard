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
    # options_for_quality = filtered_df["Quality"].tolist()
    # search_criteria_quality = st.selectbox("Select your quality:", options_for_quality)
    




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
total_sales=filtered_df["Sales Quantity Single"].sum() + filtered_df["Sales Quantity ply"].sum()
formatted_total_sales="{:.2f}".format(total_sales)




col1,col2,col3,col4,col5=st.columns((5))

if not factory and not millno:

    with col1:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Pallet</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_pallet}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        

    with col2:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Truss</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_truss}</p>'
        st.markdown(value,unsafe_allow_html=True)
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
        
        

    with col4:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_mton}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        

    with col5:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Total Sales</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_total_sales}</p>'
        st.markdown(value,unsafe_allow_html=True)
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
        

    with col2:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Truss</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_truss}</p>'
        st.markdown(value,unsafe_allow_html=True)
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
        
        

    with col4:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_mton}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        
    

    with col5:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Total Sales</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_total_sales}</p>'
        st.markdown(value,unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
       

# end sections for text columns
    


col1,col2,col3=st.columns((3))



# Group by Opening stock and sum the production for each category
grouped_df = filtered_df.groupby("Date").agg({
    "Opening Stock Pallet": "sum",
    "Opening Stock Truss": "sum",
    "Opening Stock Carton": "sum",
    "Opening Stock M/Ton": "sum"
}).reset_index()

# # Define the data for each bar chart
data = [
    go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock Pallet"], name="Opening Stock Pallet", text=["{:.2f}".format(value) for value in grouped_df["Opening Stock Pallet"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock Truss"], name="Opening Stock Truss",text=["{:.2f}".format(value) for value in grouped_df["Opening Stock Truss"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock Carton"], name="Opening Stock Carton",text=["{:.2f}".format(value) for value in grouped_df["Opening Stock Carton"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock M/Ton"], name="Opening Stock M/Ton",text=["{:.2f}".format(value) for value in grouped_df["Opening Stock M/Ton"]], textposition="auto")
]

# # Define the layout
layout = go.Layout(title="Opening Stock",
                   xaxis=dict(title="Date"),
                   yaxis=dict(title="Opening Stock"),
                   barmode="group")

# # Create the figure
fig = go.Figure(data=data, layout=layout)

# # Display the chart in Streamlit
st.plotly_chart(fig,use_container_width=True)




# Group by despatch and sum the production for each category
grouped_df = filtered_df.groupby("Date").agg({
    "Despatch Pallet": "sum",
    "Despatch Truss": "sum",
    "Despatch Carton": "sum",
    "Despatch M/Ton": "sum"
}).reset_index()

# # Define the data for each bar chart
data = [
    go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch Pallet"], name="Despatch Pallet", text=["{:.2f}".format(value) for value in grouped_df["Despatch Pallet"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch Truss"], name="Despatch Truss", text=["{:.2f}".format(value) for value in grouped_df["Despatch Truss"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch Carton"], name="Despatch Carton", text=["{:.2f}".format(value) for value in grouped_df["Despatch Carton"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch M/Ton"], name="Despatch M/Ton", text=["{:.2f}".format(value) for value in grouped_df["Despatch M/Ton"]], textposition="auto")
]

# # Define the layout
layout = go.Layout(title="Despatch",
                   xaxis=dict(title="Date"),
                   yaxis=dict(title="Despatch"),
                   barmode="group")

# # Create the figure
fig = go.Figure(data=data, layout=layout)

# # Display the chart in Streamlit
st.plotly_chart(fig,use_container_width=True)




# Group by despatch and sum the production for each category
grouped_df = filtered_df.groupby("Date").agg({
    "Closing Stock Pallet": "sum",
    "Closing Stock Truss": "sum",
    "Closing Stock Carton": "sum",
    "Closing Stock M/Ton": "sum"
}).reset_index()

# # Define the data for each bar chart
data = [
    go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock Pallet"], name="Closing Stock Pallet", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock Pallet"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock Truss"], name="Closing Stock Truss", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock Truss"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock Carton"], name="Closing Stock Carton", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock Carton"]], textposition="auto"),
    go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock M/Ton"], name="Closing Stock M/Ton", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock M/Ton"]], textposition="auto")
]

# # Define the layout
layout = go.Layout(title="Closing Stock",
                   xaxis=dict(title="Date"),
                   yaxis=dict(title="Closing Stock"),
                   barmode="group")

# # Create the figure
fig = go.Figure(data=data, layout=layout)

# # Display the chart in Streamlit
st.plotly_chart(fig,use_container_width=True)