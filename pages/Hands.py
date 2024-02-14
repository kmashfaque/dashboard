import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult

warnings.filterwarnings("ignore")


st.set_page_config(page_title="Hands Per Ton", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Hands Per Ton")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)




# file uploading section
# fl=st.file_uploader(":file_folder: Upload a file", type=(["csv","xlsx","txt","xls"]))
# if fl is not None:
#     filename=fl.name
#     st.write(filename)
#     hands_df=pd.read_excel(filename)
# else:
#     os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
    
#     hands_df=pd.read_excel("HandsPerTon.xlsx")

os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
    
hands_df=pd.read_excel("HandsPerTon.xlsx")

# date filtering starts here
col1, col2=st.columns((2))
hands_df["Date"]=pd.to_datetime(hands_df["Date"])

# getting the min and max date
startdate=pd.to_datetime(hands_df["Date"]).min()
enddate=pd.to_datetime(hands_df["Date"]).max()


with col1:
    date1=pd.to_datetime(st.date_input("Start Date",startdate))

with col2:
    date2=pd.to_datetime(st.date_input("End Date", enddate))

hands_df=hands_df[(hands_df["Date"]>=date1) & (hands_df["Date"]<=date2)].copy()

# date filtering section ends here



# sidebar for filtering data starts here

st.sidebar.header("Choose your filter: ")
# Create for Factory Name
factory=st.sidebar.multiselect("Pick Location",
                               hands_df["Factory"].unique(),
                               default=hands_df["Factory"].unique()
                               )

if not factory:
    hands_df2=hands_df.copy()
else:
    hands_df2=hands_df[hands_df["Factory"].isin(factory)]


# Create for mill no
millno=st.sidebar.multiselect("Choose Mill",
                              hands_df["Mill No."].unique(),
                              default=hands_df["Mill No."].unique()
                              )

if not millno:
    hands_df3=hands_df2.copy()
else:
    hands_df3=hands_df2[hands_df2["Mill No."].isin(millno)]



# Create for product type
shift=st.sidebar.multiselect("Select Shift",
                             hands_df["Shift"].unique(),
                             default=hands_df["Shift"].unique()
                             )

if not shift:
    hands_df4=hands_df3.copy()
else:
    hands_df4=hands_df3[hands_df3["Shift"].isin(shift)]

# sidebar for filtering data ends here



# # Filter the data based on shift, product type and mill no
if not factory and not millno and not shift:
    filtered_df = hands_df
elif not factory and not millno:
    filtered_df = hands_df[hands_df["Shift"].isin(shift)]
elif not shift and not factory:
    filtered_df = hands_df[hands_df["Mill No."].isin(millno)]
elif millno and shift:
    filtered_df = hands_df3[hands_df["Mill No."].isin(millno) & hands_df3["Shift"].isin(shift)]
elif shift and factory:
    filtered_df = hands_df3[hands_df["Shift"].isin(shift) & hands_df3["Factory"].isin(factory)]
elif factory and millno:
    filtered_df = hands_df3[hands_df["Factory"].isin(factory) & hands_df3["Mill No."].isin(millno)]
elif shift:
    filtered_df = hands_df3[hands_df3["Shift"].isin(shift)]
elif millno:
    filtered_df = hands_df3[hands_df3["Mill No."].isin(millno)]
elif factory:
    filtered_df = hands_df3[hands_df3["Factory"].isin(factory)]
else:
    filtered_df = hands_df3[hands_df3["Shift"].isin(shift) & hands_df3["Mill No."].isin(millno) & hands_df3["Factory"].isin(factory)]

# data filtering ends here
    

# groupby shift for data visualization
factory_df=filtered_df.groupby(filtered_df["Factory"], as_index=False)["Hands"].sum()
millwise_hands=filtered_df.groupby(filtered_df["Mill No."], as_index=False)["Hands"].sum()
factory_df_hands_per_ton=filtered_df.groupby(filtered_df["Factory"], as_index=False)["Hands Per Ton"].sum()

shift_wise_hands_per_ton=filtered_df.groupby(filtered_df["Shift"],as_index=False)["Hands Per Ton"].sum()


# shift for text columns
col1,col2=st.columns((2))

total_hands=filtered_df["Hands"].sum()
hands_per_ton=filtered_df["Hands Per Ton"].sum()

if not factory and not millno and not shift:
    # total_hands=filtered_df["Hands"].sum()
    # hands_per_ton=filtered_df["Hands Per Ton"].sum()

    with col1:
        formatted_total_hands="{:.2f}".format(total_hands)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Total Hands</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 20px; font-weight:bold;">{formatted_total_hands}</p>'
        st.markdown(value,unsafe_allow_html=True)

    with col2:

        formatted_total_hands="{:.2f}".format(hands_per_ton)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Hands Per Ton</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 20px; font-weight:bold;">{formatted_total_hands}</p>'
        st.markdown(value,unsafe_allow_html=True)
       
    
    
else:
    with col1:
        formatted_total_hands="{:.2f}".format(total_hands)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Total Hands</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 20px; font-weight:bold;">{formatted_total_hands}</p>'
        st.markdown(value,unsafe_allow_html=True)
       

    with col2:
        formatted_total_hands="{:.2f}".format(hands_per_ton)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Hands Per Ton</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 20px; font-weight:bold;">{formatted_total_hands}</p>'
        st.markdown(value,unsafe_allow_html=True)
       

# end section for text columns



# starts section for charts
col1,col2=st.columns((2))
with col1:
    try:
        # original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Factory Wise Hands</p>'
    # st.markdown(original_title,unsafe_allow_html=True)
    
        fig=px.bar(factory_df,x="Factory",y="Hands",text=['{:,.2f}'.format(x) for x in factory_df["Hands"]],
                    template = "seaborn",height=350,width=350)
        fig.update_layout(title="Factory Wise Hands ")
    
    except IndexError:
        st.warning("No data found for the specified filter.")
        
    if "fig" in locals():

        st.plotly_chart(fig,use_container_width=False, )

with col2:

    try:
            
        # original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Factory wise Hands Per Ton</p>'
        # st.markdown(original_title,unsafe_allow_html=True)
        fig = px.bar(factory_df_hands_per_ton, x="Factory",y="Hands Per Ton",text=['{:,.2f}'.format(x) for x in factory_df_hands_per_ton["Hands Per Ton"]],
                    template="seaborn",height=350,width=350)
        fig.update_layout(title="Factory Wise Hands Per Ton")
    
    except IndexError:
        st.warning("No data found for the specified filter.")


    if "fig" in locals():
        st.plotly_chart(fig,use_container_width=False)


# section for department wise hands per ton

# st.subheader("Department wise Hands")

# Define the list of selected departments
selected_departments = ["Spreader", "Breaker", "Drawing", "Spinning", "Finisher", "Roll Winding", "Precision Winding"]
selected_departments_mechanical = ["Mechanical"]
selected_departments_quality = ["Quality"]
selected_departments_production_general = ["Production General"]

# Filter the DataFrame to include only the selected departments
selected_df = filtered_df[filtered_df["Section"].isin(selected_departments)]

# Group by "Section" (department) and sum the values of "Hands" for each department
production_department = selected_df.groupby("Section")["Hands"].sum().reset_index()

# Filter the DataFrame to include only the mechanical department
selected_df_mechanical = filtered_df[filtered_df["Section"].isin(selected_departments_mechanical)]
mechanical_dept = selected_df_mechanical["Hands"].sum()

# Filter the DataFrame to include only the quality department
selected_df_quality = filtered_df[filtered_df["Section"].isin(selected_departments_quality)]
quality_dept = selected_df_quality["Hands"].sum()

# Filter the DataFrame to include only the production general department
selected_df_production_general = filtered_df[filtered_df["Section"].isin(selected_departments_production_general)]
production_general_dept = selected_df_production_general["Hands"].sum()

# Create a DataFrame to concatenate the sums
combined_df = pd.DataFrame({
    "Section": ["Production"] * len(production_department) + ["Mechanical"] + ["Quality"] + ["Production General"],
    "Hands": production_department["Hands"].tolist() + [mechanical_dept] + [quality_dept] + [production_general_dept]
})

# Create a pie chart for the combined data
fig_combined = px.pie(combined_df, values="Hands", names="Section", hole=0.5)

# Update layout
fig_combined.update_layout(title="Total Hands by Department")

# Display the combined pie chart using Streamlit
st.plotly_chart(fig_combined, use_container_width=True)