import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import base64
from io import BytesIO


warnings.filterwarnings("ignore")



os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
df=pd.read_excel("production.xlsx")
hands_df=pd.read_excel("HandsPerTon.xlsx")
stock_df=pd.read_excel("Stocks.xlsx")

unique_date=df["Date"].unique()
hands_df=hands_df[hands_df["Date"].isin(unique_date)]
stock_df=stock_df[stock_df["Date"].isin(unique_date)]

# Extract the end date from the DataFrame
end_date_from_df = df["Date"].max().strftime('%Y-%m-%d')
st.set_page_config(page_title="Production Dashboard!!", page_icon=":bar_chart:", layout="wide")

title_with_end_date = f":bar_chart: Daily Production Dashboard - Date: {end_date_from_df}"
st.title(title_with_end_date)
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")

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

    
# df=pd.read_excel("production.xlsx")
# hands_df=pd.read_excel("HandsPerTon.xlsx")
# stock_df=pd.read_excel("Stocks.xlsx")

# unique_date=df["Date"].unique()
# hands_df=hands_df[hands_df["Date"].isin(unique_date)]
# stock_df=stock_df[stock_df["Date"].isin(unique_date)]







# Sidebar for filtering data
st.sidebar.header("Choose your filter:")
# Create for Factory Name
selected_factory = st.sidebar.selectbox("Pick Location",
                                        ["All"] + list(df["Factory"].unique()),
                                        index=0)


# Define the function to generate a download link for Excel
def get_table_download_link(df, filename):
    excel_file_buffer = BytesIO()
    df.to_excel(excel_file_buffer, index=False)
    excel_file_buffer.seek(0)
    b64 = base64.b64encode(excel_file_buffer.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">Download file</a>'
    return href


if selected_factory=="All":
    factory_df_selected=df
    with st.expander("View DataFrame"):
        # Display the DataFrame within the expander
        st.write(factory_df_selected)
        # Generate a download button for the DataFrame
else:
    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    

    with st.expander("View DataFrame"):
        # Display the DataFrame within the expander
        st.write(factory_df_selected)
        # Generate a download button for the DataFrame
        

st.markdown(get_table_download_link(factory_df_selected, "production"), unsafe_allow_html=True)

st.markdown("")


# filter data based on factory

col1,col2,col3,col4,col5,col6=st.columns((6))



if selected_factory=="All":


    factory_df=df
    hands_df_all=hands_df
    stock_all=stock_df
    actual_production=factory_df["achieved production"].sum()
    efficiency=factory_df["Efficiency"].mean()
    converted_production=factory_df["Converted Production"].sum()
    total_frame=factory_df["frame"].sum()
    total_hands=hands_df["Hands Per Ton"].sum()
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
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center;">Target</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center;">{formatted_actual_production}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")
          

        with col1_actual:
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Achieved</p>'
            st.markdown(original_title,unsafe_allow_html=True)

            

            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_actual_production}</p>'
            st.markdown(value,unsafe_allow_html=True)

            st.markdown("")
            st.markdown("")
            st.markdown("")

    with col2:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Efficiency</p>'
        st.markdown(original_title,unsafe_allow_html=True)

       
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Achieved</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
        st.markdown(value, unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
    with col3:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Converted Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)

        
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Achieved</p>'
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
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Hands Per Ton</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Premises Wise</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_total_hands}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")


        with col6:
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Premises Wise</p>'
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
    actual_production=factory_df_selected["achieved production"].sum()
    efficiency=factory_df_selected["Efficiency"].mean()
    converted_production=factory_df_selected["Converted Production"].sum()
    total_frame=factory_df_selected["frame"].sum()
    total_hands=hands_df_selected["Hands Per Ton"].sum()
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

       
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Achieved</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
        st.markdown(value, unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")
       
    

    with col3:
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Converted Production</p>'
        st.markdown(original_title,unsafe_allow_html=True)

        
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Achieved</p>'
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
            
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Hands Per Ton</p>'
            st.markdown(original_title,unsafe_allow_html=True)
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Premises Wise</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_total_hands}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")

    
    with col6:
           
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center;">Despatch</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Premises Wise</p>'
            st.markdown(original_title,unsafe_allow_html=True)
            value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{formatted_stock_despatch}</p>'
            st.markdown(value,unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            st.markdown("")


    
# end sections for text columns

# Function to create a styled card
# def create_card(title, value):
#     card = f"""
#     <div style="background-color: #f0f0f0; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
#         <p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold; text-align:center;">{title}</p>
#         <p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold; text-align:center;">{value}</p>
#     </div>
#     """
#     return card

# # Display the cards for each column
# with col1:
#     st.markdown(create_card("Production", formatted_actual_production), unsafe_allow_html=True)

# with col2:
#     st.markdown(create_card("Efficiency", formatted_efficiency), unsafe_allow_html=True)

# with col3:
#     st.markdown(create_card("Converted Production", formatted_converted_production), unsafe_allow_html=True)

# with col4:
#     st.markdown(create_card("Total Frame", total_frame), unsafe_allow_html=True)

# with col5:
#     st.markdown(create_card("Hands Per Ton", formatted_total_hands), unsafe_allow_html=True)

# with col6:
#     st.markdown(create_card("Despatch", formatted_stock_despatch), unsafe_allow_html=True)


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
#         fig=px.bar(factory_df,x="Factory",y="actual production",text=['{:,.2f}'.format(x) for x in factory_df["achieved production"]],
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
    factory_df = df.groupby(df["Factory"], as_index=False)["achieved production"].sum()
    efficiency_df = df.groupby(df["Factory"], as_index=False)["Efficiency"].mean()
    hands_per_ton_df = hands_df.groupby(hands_df["Factory"], as_index=False)["Hands Per Ton"].sum()
    with col1:
        try:
            # Create a bar chart for production by factory
            fig = px.bar(factory_df, x="Factory", y="achieved production", text=['{:,.2f}'.format(x) for x in factory_df["achieved production"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(factory_df))
            fig.update_layout(title="Production: Premises Wise")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        
        # Convert efficiency values to percentages
        efficiency_df["Efficiency (%)"] = efficiency_df["Efficiency"] * 100
        try:
            # Create a bar chart for efficiency by mill number
            fig = px.bar(efficiency_df, x="Factory", y="Efficiency (%)",
                         text=['{:,.0f}%'.format(x) for x in efficiency_df["Efficiency (%)"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #1C4E80"] * len(efficiency_df))
            fig.update_layout(title="Efficiency: Premises Wise")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col3:
        try:
            # Create a bar chart for hands per ton by factory
            fig = px.bar(hands_per_ton_df, x="Factory", y="Hands Per Ton", text=['{:,.2f}'.format(x) for x in hands_per_ton_df["Hands Per Ton"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=["#AC3E31"] * len(hands_per_ton_df))
            fig.update_layout(title="Hands Per Ton: Premises Wise")
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
    mill_production_df = mill_df.groupby(["Mill No."], as_index=False)["achieved production"].sum()
    mill_efficiency_df = mill_df.groupby(["Mill No."], as_index=False)["Efficiency"].mean()
    mill_hands_per_ton_df = hands_mill_no.groupby(["Mill No."], as_index=False)["Hands Per Ton"].sum()

  

    with col1:
        
        try:
            # Create a bar chart for production by mill number
            fig = px.bar(mill_production_df, x="Mill No.", y="achieved production",
                         text=['{:,.2f}'.format(x) for x in mill_production_df["achieved production"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #488A99"] * len(mill_production_df))
            fig.update_layout(title="Production: Mill Wise")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        # Convert efficiency values to percentages
        mill_efficiency_df["Efficiency (%)"] = mill_efficiency_df["Efficiency"] * 100
        try:
            # Create a bar chart for efficiency by mill number
            fig = px.bar(mill_efficiency_df, x="Mill No.", y="Efficiency (%)",
                         text=['{:,.0f}%'.format(x) for x in mill_efficiency_df["Efficiency (%)"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #1C4E80"] * len(mill_efficiency_df))
            fig.update_layout(title="Efficiency: Mill Wise")
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
            fig.update_layout(title="Hands Per Ton: Mill Wise")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")




# counwise production chart

if selected_factory=="All":
    count_df = df.groupby(df["count"], as_index=False)["achieved production"].sum()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(count_df, x="count", y="achieved production", text=['{:,.2f}'.format(x) for x in count_df["achieved production"]],
        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
        fig.update_layout(title="Production: Countwise")
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
    mill_production_df = mill_df.groupby(["count"], as_index=False)["achieved production"].sum()
    
  
    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_production_df, x="count", y="achieved production",
        text=['{:,.2f}'.format(x) for x in mill_production_df["achieved production"]],
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