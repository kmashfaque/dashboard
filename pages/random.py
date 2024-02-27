



import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import plotly.graph_objs as go
import streamlit as st
import pandas as pd
import base64
from io import BytesIO

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Over All Production!!", page_icon=":bar_chart:", layout="wide")




st.title(" :bar_chart: Production Details Dashboard")
st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)

with open("pages\style.css")as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

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


# Load the DataFrame
df = pd.read_excel("production.xlsx", sheet_name="Overall Production")
unique_date=df["Date"]









# # date filtering starts here
col1, col2=st.columns((2))
df["Date"]=pd.to_datetime(df["Date"])

# getting the min and max date
startdate=pd.to_datetime(df["Date"]).min()
enddate=pd.to_datetime(df["Date"]).max()


with col1:
    date1=pd.to_datetime(st.date_input("Start Date",startdate))

with col2:
    date2=pd.to_datetime(st.date_input("End Date", enddate))

df=df[(df["Date"]>=date1) & (df["Date"]<=date2)].copy()

# date filtering section ends here




# Sidebar for filtering data
st.sidebar.header("Choose your filter:")
# Create for Factory Name
selected_factory = st.sidebar.selectbox("Pick Location",
                                        ["All"] + list(df["Factory"].unique()),
                                        index=0)

# Filter mill numbers based on the selected factory
if selected_factory == "All":
    filtered_mill_numbers = df["Mill No."].unique()
  
    
else:
    filtered_mill_numbers = df[df["Factory"] == selected_factory]["Mill No."].unique()



 # Create a selectbox for Mill Name
selected_mill_number = st.sidebar.selectbox("Pick Mill No.",
                                                ["All"] + list(filtered_mill_numbers),
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
    factory_df=df
    with st.expander("View DataFrame"):
        # Display the DataFrame within the expander
        st.write(factory_df)
        # Generate a download button for the DataFrame
else:
    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    

    with st.expander("View DataFrame"):
        # Display the DataFrame within the expander
        st.write(factory_df_selected)
        # Generate a download button for the DataFrame
        

st.markdown(get_table_download_link(factory_df, "production"), unsafe_allow_html=True)



col1,col2,col3,col4,col5=st.columns(5)


if selected_factory=="All":
    factory_df=df

    production=factory_df["achieved production"].sum()
    efficiency=factory_df["Efficiency"].mean()
    converted_production=factory_df["Converted Production"].sum()
    total_frame=factory_df["Frame"].sum()

    formatted_actual_production="{:.2f}".format(production)
    formatted_efficiency="{:.0%}".format(efficiency)
    formatted_converted_production="{:.2f}".format(converted_production)

    with col1:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center;margin:0;">Production</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center;margin:0">{formatted_actual_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    

    with col2:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Efficiency</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    


    with col3:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Converted Production</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{formatted_converted_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    
    with col4:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Frame</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{total_frame}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")


else:
    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from the selected factory DataFrame
    selected_mills_production = factory_df_selected["Mill No."].unique()

    # Filter the DataFrame to include only the selected mills
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

    if selected_mill_number=="All":
        production=factory_df_selected["achieved production"].sum()
        efficiency=factory_df_selected["Efficiency"].mean()
        converted_production=factory_df_selected["Converted Production"].sum()
        total_frame=factory_df_selected["Frame"].sum()

        formatted_actual_production="{:.2f}".format(production)
        formatted_efficiency="{:.0%}".format(efficiency)
        formatted_converted_production="{:.2f}".format(converted_production)

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        
        production = mill_df_selected["achieved production"].sum()
        efficiency = mill_df_selected["Efficiency"].mean()
        converted_production = mill_df_selected["Converted Production"].sum()
        total_frame = mill_df_selected["Frame"].sum()

        formatted_actual_production="{:.2f}".format(production)
        formatted_efficiency="{:.0%}".format(efficiency)
        formatted_converted_production="{:.2f}".format(converted_production)



    with col1:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Production</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{formatted_actual_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    

    with col2:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Efficiency</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{formatted_efficiency}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    


    with col3:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Converted Production</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{formatted_converted_production}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
    
    with col4:


        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 14px; font-weight:bold;text-align:center">Frame</p>'
        
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 14px; font-weight:bold;text-align:center">{total_frame}</p>'
        st.markdown(value,unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        st.markdown("")
   
    


# Start sections for charts
col1, col2, col3 = st.columns((3))

# Display factory-wise charts
import plotly.express as px

if selected_factory == "All":
    factory_df = df.groupby(df["Factory"], as_index=False)["achieved production"].sum()
    efficiency_df = df.groupby(df["Factory"], as_index=False)["Efficiency"].mean()
    ply_df = df.groupby(df["Ply"], as_index=False)["achieved production"].sum()

    with col1:
        try:
            # Create a bar chart for production by factory
            fig = px.bar(
                factory_df,
                x="Factory",
                y="achieved production",
                text=["{:,.2f}".format(x) for x in factory_df["achieved production"]],
                template="seaborn",
                width=350,
                height=350,
                color=factory_df["Factory"],  # Assigning different colors based on the "Factory" column
            )
            fig.update_layout(title="Production ")
            fig.update_traces(textfont_color='white')  # Setting text color to white
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        try:
            # Create a bar chart for efficiency by factory
            fig = px.bar(
                efficiency_df,
                x="Factory",
                y="Efficiency",
                text=["{:,.2f}".format(x) for x in efficiency_df["Efficiency"]],
                template="seaborn",
                width=350,
                height=350,
                color=efficiency_df["Factory"],  # Assigning different colors based on the "Factory" column
            )
            fig.update_layout(title="Efficiency ")
            fig.update_traces(textfont_color='white')  # Setting text color to white
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col3:

        try:
            # Create a bar chart for production by factory
            fig = px.bar(
                ply_df,
                x="Ply",
                y="achieved production",
                text=["{:,.2f}".format(x) for x in ply_df["achieved production"]],
                template="seaborn",
                width=350,
                height=350,
                color=ply_df["Ply"],  # Assigning different colors based on the "Ply" column
            )
            fig.update_layout(title="Ply")
            fig.update_traces(textfont_color='white')  # Setting text color to white
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")


# Display mill-wise data if a factory is selected
else:

    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from the selected factory DataFrame
    selected_mills_production = factory_df_selected["Mill No."].unique()

    # Filter the DataFrame to include only the selected mills
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

    if selected_mill_number=="All":
        mill_ply_df = factory_df_selected.groupby(["Ply"], as_index=False)["achieved production"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["Ply"].unique()
        mill_df_ply = mill_df_selected[mill_df_selected["Ply"].isin(selected_mills)]
        mill_ply_df = mill_df_ply.groupby(["Ply"], as_index=False)["achieved production"].sum()

   
    
    mill_production_df = mill_df.groupby(["Mill No."], as_index=False)["achieved production"].sum()
    mill_efficiency_df = mill_df.groupby(["Mill No."], as_index=False)["Efficiency"].mean()

  


    with col1:
        try:
            # Create a bar chart for production by mill number
            fig = px.bar(mill_production_df, x="Mill No.", y="achieved production",
                         text=['{:,.2f}'.format(x) for x in mill_production_df["achieved production"]],
                         template="seaborn", width=350, height=350,
                         color_discrete_sequence=[" #488A99"] * len(mill_production_df))
            fig.update_layout(title="Production")
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
            fig.update_layout(title="Efficiency ")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col3:
        try:
            fig = px.bar(mill_ply_df, x="Ply", y="achieved production", 
                         text=['{:,.2f}'.format(x) for x in mill_ply_df["achieved production"]],
                         template="seaborn", width=700, height=350,
                         color_discrete_sequence=[" #488A99"] * len(mill_ply_df))
            fig.update_layout(title="Ply")
            st.plotly_chart(fig, use_container_width=True)


        except IndexError:
            st.warning("No data found for the specified filter.")


# quality wise chart

if selected_factory=="All":
    quality_df = df.groupby(df["Product Type"], as_index=False)["achieved production"].sum()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(quality_df, x="Product Type", y="achieved production", text=['{:,.2f}'.format(x) for x in quality_df["achieved production"]],
        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(quality_df))
        fig.update_layout(title="Quality vs Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
            st.warning("No data found for the specified filter.")

    

# Display mill-wise data if a factory is selected
else:


    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from the selected factory DataFrame
    selected_mills_production = factory_df_selected["Mill No."].unique()

    # Filter the DataFrame to include only the selected mills
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

    if selected_mill_number=="All":
        mill_count_df = mill_df.groupby(["Product Type"], as_index=False)["achieved production"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["Product Type"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["Product Type"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["Product Type"], as_index=False)["achieved production"].sum()

    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_count_df, x="Product Type", y="achieved production",
        text=['{:,.2f}'.format(x) for x in mill_count_df["achieved production"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Quality vs Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")

# end quality chart
        

    

# counwise production chart

if selected_factory=="All":
    count_df = df.groupby(df["count"], as_index=False)["achieved production"].sum()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(count_df, x="count", y="achieved production", text=['{:,.2f}'.format(x) for x in count_df["achieved production"]],
        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
        fig.update_layout(title="Countwise Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
            st.warning("No data found for the specified filter.")

    

# Display mill-wise data if a factory is selected
else:

  
    # new


    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from the selected factory DataFrame
    selected_mills_production = factory_df_selected["Mill No."].unique()

    # Filter the DataFrame to include only the selected mills
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

    if selected_mill_number=="All":
        mill_count_df = mill_df.groupby(["count"], as_index=False)["achieved production"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["count"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["count"], as_index=False)["achieved production"].sum()

   
    

  
    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_count_df, x="count", y="achieved production",
        text=['{:,.2f}'.format(x) for x in mill_count_df["achieved production"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Countwise Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")

   




# # frame vs count chart

# if selected_factory=="All":
#     count_df = df.groupby(df["count"], as_index=False)["Frame"].sum()
    
#     try:
#         # Create a bar chart for production by factory
#         fig = px.bar(count_df, x="count", y="Frame", text=['{:,.2f}'.format(x) for x in count_df["Frame"]],
#         template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
#         fig.update_layout(title="Frame vs Count")
#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#             st.warning("No data found for the specified filter.")

    

# # Display mill-wise data if a factory is selected
# else:

  
#     # new


#     selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

#     # Filter the DataFrame based on the selected factories
#     factory_df_selected = df[df['Factory'].isin(selected_factory)]

#     # Extract unique mill numbers from the selected factory DataFrame
#     selected_mills_production = factory_df_selected["Mill No."].unique()

#     # Filter the DataFrame to include only the selected mills
#     mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

#     if selected_mill_number=="All":
#         mill_count_df = mill_df.groupby(["count"], as_index=False)["Frame"].sum()

#     else:

#         # Group by both mill number to get production data for ply
#         selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
#         mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
#         selected_mills = mill_df_selected["count"].unique()
#         mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
#         mill_count_df = mill_df_count.groupby(["count"], as_index=False)["Frame"].sum()

   
    

  
#     try:
#         # Create a bar chart for production by mill number
#         fig = px.bar(mill_count_df, x="count", y="Frame",
#         text=['{:,.2f}'.format(x) for x in mill_count_df["Frame"]],
#         template="seaborn", width=1000, height=500,
#         color_discrete_sequence=[" #488A99"] * len(mill_count_df))
#         fig.update_layout(title="Frame vs Count")
#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#         st.warning("No data found for the specified filter.")


# # efficiency vs count chart

# if selected_factory=="All":
#     count_df = df.groupby(df["count"], as_index=False)["Efficiency"].mean()
    
#     try:
#         # Create a bar chart for production by factory
#         fig = px.bar(count_df, x="count", y="Efficiency", text=['{:,.2f}'.format(x) for x in count_df["Efficiency"]],
#         template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
#         fig.update_layout(title="Efficiency vs Count")
#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#             st.warning("No data found for the specified filter.")

    

# # Display mill-wise data if a factory is selected
# else:


#     selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

#     # Filter the DataFrame based on the selected factories
#     factory_df_selected = df[df['Factory'].isin(selected_factory)]

#     # Extract unique mill numbers from the selected factory DataFrame
#     selected_mills_production = factory_df_selected["Mill No."].unique()

#     # Filter the DataFrame to include only the selected mills
#     mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

#     if selected_mill_number=="All":
#         mill_count_df = mill_df.groupby(["count"], as_index=False)["Efficiency"].mean()

#     else:

#         # Group by both mill number to get production data for ply
#         selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
#         mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
#         selected_mills = mill_df_selected["count"].unique()
#         mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
#         mill_count_df = mill_df_count.groupby(["count"], as_index=False)["Efficiency"].mean()

  
#     try:
#         # Create a bar chart for production by mill number
#         fig = px.bar(mill_count_df, x="count", y="Efficiency",
#         text=['{:,.2f}'.format(x) for x in mill_count_df["Efficiency"]],
#         template="seaborn", width=1000, height=500,
#         color_discrete_sequence=[" #488A99"] * len(mill_count_df))
#         fig.update_layout(title="Efficiency vs Count")
#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#         st.warning("No data found for the specified filter.")



# # frame with count vs production 
        
# # if selected_factory == "All":
# #     count_df = df.groupby(df["count"], as_index=False)["achieved production"].sum()
    
# #     try:
# #         # Create a bar chart for production by factory
# #         fig = px.bar(count_df, x="count", y="achieved production", 
# #                      text=['{:,.2f}'.format(x) for x in count_df["achieved production"]],
# #                      template="seaborn", width=1000, height=500, 
# #                      color_discrete_sequence=[" #488A99"] * len(count_df))
# #         fig.update_layout(title="Countwise Production")
        
# #         # Add scatter plot for frame data
# #         frame_data = df.groupby("count", as_index=False)["Frame"].sum()
# #         fig.add_trace(go.Scatter(x=frame_data["count"], y=frame_data["Frame"], 
# #                                  mode="markers", name="Frame Data", marker=dict(color="red", size=10)))

# #         # Add frame data as text annotations
# #         for i, row in frame_data.iterrows():
# #             fig.add_annotation(x=row["count"], y=row["Frame"], text=f'{row["Frame"]:.2f}',
# #                                font=dict(color='white', size=12), showarrow=True, arrowhead=1)

# #         st.plotly_chart(fig, use_container_width=True)

# #     except IndexError:
# #         st.warning("No data found for the specified filter.")

# # # Display mill-wise data if a factory is selected
# # else:
# #     selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

# #     # Filter the DataFrame based on the selected factories
# #     factory_df_selected = df[df['Factory'].isin(selected_factory)]

# #     # Extract unique mill numbers from the selected factory DataFrame
# #     selected_mills_production = factory_df_selected["Mill No."].unique()

# #     # Filter the DataFrame to include only the selected mills
# #     mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]

# #     if selected_mill_number == "All":
# #         mill_count_df = mill_df.groupby(["count"], as_index=False)["achieved production"].sum()
# #     else:
# #         # Group by both mill number to get production data for ply
# #         selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
# #         mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
# #         selected_mills = mill_df_selected["count"].unique()
# #         mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
# #         mill_count_df = mill_df_count.groupby(["count"], as_index=False)["achieved production"].sum()

# #     try:
# #         # Create a bar chart for production by mill number
# #         fig = px.bar(mill_count_df, x="count", y="achieved production",
# #                      text=['{:,.2f}'.format(x) for x in mill_count_df["achieved production"]],
# #                      template="seaborn", width=1000, height=500,
# #                      color_discrete_sequence=[" #488A99"] * len(mill_count_df))
# #         fig.update_layout(title="Countwise Production")

# #         # Add scatter plot for frame data
# #         frame_data = mill_df.groupby("count", as_index=False)["Frame"].sum()
# #         fig.add_trace(go.Scatter(x=frame_data["count"], y=frame_data["Frame"],
# #                                  mode="markers", name="Frame Data", marker=dict(color="red", size=10)))

# #         # Add frame data as text annotations
# #         for i, row in frame_data.iterrows():
# #             fig.add_annotation(x=row["count"], y=row["Frame"], text=f'{row["Frame"]:.2f}',
# #                                font=dict(color='white', size=12), showarrow=True, arrowhead=1)

# #         st.plotly_chart(fig, use_container_width=True)

# #     except IndexError:
# #         st.warning("No data found for the specified filter.")


# # import streamlit as st
# # import plotly.express as px
# # import pandas as pd
# # import os
# # import warnings
# # import matplotlib as mult
# # import plotly.graph_objs as go

# # warnings.filterwarnings("ignore")


# # st.set_page_config(page_title="Overall Stock", page_icon=":bar_chart:", layout="wide")
# # st.title(" :bar_chart: Overall Stock")
# # st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)


# # os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")
    
# # stock_df=pd.read_excel("Stocks.xlsx")


# # # sidebar for filtering data starts here
# # st.sidebar.header("Choose your filter: ")
# # # Create for Factory Name
# # factory=st.sidebar.multiselect("Pick Factory",
# #                                stock_df["Factory"].unique(),
# #                                default=stock_df["Factory"].unique()
# #                                )

# # if not factory:
# #     df2=stock_df.copy()
# # else:
# #     df2=stock_df[stock_df["Factory"].isin(factory)]


# # # Create for mill no
# # millno=st.sidebar.multiselect("Choose Mill No.",
# #                               stock_df["Mill No."].unique(),
# #                               default=stock_df["Mill No."].unique()
# #                               )

# # if not millno:
# #     df3=df2.copy()
# # else:
# #     df3=df2[df2["Mill No."].isin(millno)]




# # # date filtering starts here
# # col1, col2=st.columns((2))
# # stock_df["Date"]=pd.to_datetime(stock_df["Date"])

# # # getting the min and max date
# # startdate=pd.to_datetime(stock_df["Date"]).min()
# # enddate=pd.to_datetime(stock_df["Date"]).max()

# # with col1:
# #     date1=pd.to_datetime(st.date_input("Start Date",startdate))

# # with col2:
# #     date2=pd.to_datetime(st.date_input("End Date", enddate))

# # stock_df=stock_df[(stock_df["Date"]>=date1) & (stock_df["Date"]<=date2)].copy()

# # # date filtering section ends here



# # # # Filter the data based on quality, product type and mill no
# # if not factory and not millno:
# #     filtered_df= stock_df
# # elif factory and millno:
# #     filtered_df = df3[stock_df["Factory"].isin(factory) & df3["Mill No."].isin(millno)]
# # elif millno:
# #     filtered_df = df3[df3["Mill No."].isin(millno)]
# # elif factory:
# #     filtered_df = df3[df3["Factory"].isin(factory)]
# # else:
# #     df3["Mill No."].isin(millno) & df3["Factory"].isin(factory)

# # # data filtering ends here



# # # Dropdown for contact number
# # # col1, col2 = st.columns((1, 3))
# # # with col1:
# # options_for_contactId = ["Select"] + filtered_df["Cont. No"].unique().tolist()
# # search_criteria_cont_no = st.selectbox("Select you contact number: ", options_for_contactId)

# # # with col2:
# # if search_criteria_cont_no != "Select":
# #     # Filter the data based on the selected contact number
# #     filtered_df = filtered_df[filtered_df["Cont. No"] == search_criteria_cont_no]

# # #         # Dropdown for quality based on the filtered data
# #     # options_for_quality = filtered_df["Quality"].tolist()
# #     # search_criteria_quality = st.selectbox("Select your quality:", options_for_quality)
    




# # # data

# # # section for text columns
# # col1,col2,col3,col4,col5,col6,col7,col8=st.columns((8))
# # production_pallet=filtered_df["Production Pallet"].sum()
# # production_truss=filtered_df["Production Truss"].sum()
# # production_carton=filtered_df["Production Carton"].sum()
# # production_mton=filtered_df["Production M/Ton"].sum()
# # formatted_production_pallet="{:.2f}".format(production_pallet)
# # formatted_production_truss="{:.2f}".format(production_truss)
# # formatted_production_carton="{:.2f}".format(production_carton)
# # formatted_production_mton="{:.2f}".format(production_mton)
# # total_sales=filtered_df["Sales Quantity Single"].sum() + filtered_df["Sales Quantity ply"].sum()
# # formatted_total_sales="{:.2f}".format(total_sales)




# # col1,col2,col3,col4,col5=st.columns((5))

# # if not factory and not millno:

# #     with col1:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Pallet</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_pallet}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        

# #     with col2:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Truss</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_truss}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        

# #     with col3:
# #     # Set a custom color scheme
# #     # original_title = '<p style="font-family:Ssns-Serif; color:Black; font-size: 18px; font-weight:bold;">Factory wise achieved production</p>'
# #     # st.markdown(original_title,unsafe_allow_html=True)
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Carton</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_carton}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        
        

# #     with col4:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Production</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_mton}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        

# #     with col5:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Total Sales</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_total_sales}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        
        

# # else:
# #     with col1:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Pallet</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_pallet}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        

# #     with col2:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Truss</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_truss}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        

# #     with col3:
# #     # Set a custom color scheme
# #     # original_title = '<p style="font-family:Ssns-Serif; color:Black; font-size: 18px; font-weight:bold;">Factory wise achieved production</p>'
# #     # st.markdown(original_title,unsafe_allow_html=True)
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Carton</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_carton}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        
        

# #     with col4:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Production</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_production_mton}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
        
    

# #     with col5:
# #         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;">Total Sales</p>'
# #         st.markdown(original_title,unsafe_allow_html=True)
# #         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_total_sales}</p>'
# #         st.markdown(value,unsafe_allow_html=True)
# #         st.markdown("")
# #         st.markdown("")
       

# # # end sections for text columns
    


# # col1,col2,col3=st.columns((3))



# # # Group by Opening stock and sum the production for each category
# # grouped_df = filtered_df.groupby("Date").agg({
# #     "Opening Stock Pallet": "sum",
# #     "Opening Stock Truss": "sum",
# #     "Opening Stock Carton": "sum",
# #     "Opening Stock M/Ton": "sum"
# # }).reset_index()

# # # # Define the data for each bar chart
# # data = [
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock Pallet"], name="Opening Stock Pallet", text=["{:.2f}".format(value) for value in grouped_df["Opening Stock Pallet"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock Truss"], name="Opening Stock Truss",text=["{:.2f}".format(value) for value in grouped_df["Opening Stock Truss"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock Carton"], name="Opening Stock Carton",text=["{:.2f}".format(value) for value in grouped_df["Opening Stock Carton"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Opening Stock M/Ton"], name="Opening Stock M/Ton",text=["{:.2f}".format(value) for value in grouped_df["Opening Stock M/Ton"]], textposition="auto")
# # ]

# # # # Define the layout
# # layout = go.Layout(title="Opening Stock",
# #                    xaxis=dict(title="Date"),
# #                    yaxis=dict(title="Opening Stock"),
# #                    barmode="group")

# # # # Create the figure
# # fig = go.Figure(data=data, layout=layout)

# # # # Display the chart in Streamlit
# # st.plotly_chart(fig,use_container_width=True)




# # # Group by despatch and sum the production for each category
# # grouped_df = filtered_df.groupby("Date").agg({
# #     "Despatch Pallet": "sum",
# #     "Despatch Truss": "sum",
# #     "Despatch Carton": "sum",
# #     "Despatch M/Ton": "sum"
# # }).reset_index()

# # # # Define the data for each bar chart
# # data = [
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch Pallet"], name="Despatch Pallet", text=["{:.2f}".format(value) for value in grouped_df["Despatch Pallet"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch Truss"], name="Despatch Truss", text=["{:.2f}".format(value) for value in grouped_df["Despatch Truss"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch Carton"], name="Despatch Carton", text=["{:.2f}".format(value) for value in grouped_df["Despatch Carton"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Despatch M/Ton"], name="Despatch M/Ton", text=["{:.2f}".format(value) for value in grouped_df["Despatch M/Ton"]], textposition="auto")
# # ]

# # # # Define the layout
# # layout = go.Layout(title="Despatch",
# #                    xaxis=dict(title="Date"),
# #                    yaxis=dict(title="Despatch"),
# #                    barmode="group")

# # # # Create the figure
# # fig = go.Figure(data=data, layout=layout)

# # # # Display the chart in Streamlit
# # st.plotly_chart(fig,use_container_width=True)




# # # Group by despatch and sum the production for each category
# # grouped_df = filtered_df.groupby("Date").agg({
# #     "Closing Stock Pallet": "sum",
# #     "Closing Stock Truss": "sum",
# #     "Closing Stock Carton": "sum",
# #     "Closing Stock M/Ton": "sum"
# # }).reset_index()

# # # # Define the data for each bar chart
# # data = [
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock Pallet"], name="Closing Stock Pallet", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock Pallet"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock Truss"], name="Closing Stock Truss", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock Truss"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock Carton"], name="Closing Stock Carton", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock Carton"]], textposition="auto"),
# #     go.Bar(x=grouped_df["Date"], y=grouped_df["Closing Stock M/Ton"], name="Closing Stock M/Ton", text=["{:.2f}".format(value) for value in grouped_df["Closing Stock M/Ton"]], textposition="auto")
# # ]

# # # # Define the layout
# # layout = go.Layout(title="Closing Stock",
# #                    xaxis=dict(title="Date"),
# #                    yaxis=dict(title="Closing Stock"),
# #                    barmode="group")

# # # # Create the figure
# # fig = go.Figure(data=data, layout=layout)

# # # # Display the chart in Streamlit
# # st.plotly_chart(fig,use_container_width=True)
        
#         import streamlit as st
# import plotly.express as px
# import pandas as pd
# import os
# import warnings
# import matplotlib as mult
# import plotly.graph_objs as go
# import streamlit as st
# import pandas as pd
# import base64
# from io import BytesIO

# warnings.filterwarnings("ignore")

# st.set_page_config(page_title="Over All Production!!", page_icon=":bar_chart:", layout="wide")

# st.title(" :bar_chart: Production Details Dashboard")
# st.markdown("<style>div.block-container{padding-top:1rem}</style>", unsafe_allow_html=True)

# os.chdir(r"C:\Users\jashfaque\Desktop\dashboardSoft")

# Load the DataFrame
df = pd.read_excel("production.xlsx", sheet_name="Overall Production")
unique_date=df["Date"]

# Sidebar for filtering data
st.sidebar.header("Choose your filter:")
selected_factory = st.sidebar.selectbox("Pick Location", ["All"] + list(df["Factory"].unique()), index=0)

# Filter mill numbers based on the selected factory
if selected_factory == "All":
    filtered_mill_numbers = df["Mill No."].unique()
else:
    filtered_mill_numbers = df[df["Factory"] == selected_factory]["Mill No."].unique()

selected_mill_number = st.sidebar.selectbox("Pick Mill No.", ["All"] + list(filtered_mill_numbers), index=0)

# Define the function to generate a download link for Excel
def get_table_download_link(df, filename):
    excel_file_buffer = BytesIO()
    df.to_excel(excel_file_buffer, index=False)
    excel_file_buffer.seek(0)
    b64 = base64.b64encode(excel_file_buffer.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}.xlsx">Download file</a>'
    return href

# Filter the DataFrame based on the selected factories
if selected_factory=="All":
    factory_df=df
else:
    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    factory_df = factory_df_selected

# Display the DataFrame and generate a download button
with st.expander("View DataFrame", expanded=True):
    # Card-style container for the DataFrame
    with st.container():
        st.dataframe(factory_df.iloc[:, :8])  # Display only the first 8 columns
        st.markdown(get_table_download_link(factory_df, "production"), unsafe_allow_html=True)

# Define card-style container function
def card_container(title, value):
    return f'''
        <div style="border-radius: 10px; border: 2px solid #AC3E31; padding: 20px; background-color: #F5F5F5; margin-bottom: 20px;">
            <p style="font-family: Arial-Black; color: Black; font-size: 18px; font-weight: bold; text-align: center;">{title}</p>
            <p style="font-family: Arial-Black; color: #AC3E31; font-size: 18px; font-weight: bold; text-align: center;">{value}</p>
        </div>
    '''

# Calculate metrics
production = factory_df["achieved production"].sum()
efficiency = factory_df["Efficiency"].mean()
converted_production = factory_df["Converted Production"].sum()
total_frame = factory_df["Frame"].sum()

# Format metrics
formatted_production = "{:.2f}".format(production)
formatted_efficiency = "{:.0%}".format(efficiency)
formatted_converted_production = "{:.2f}".format(converted_production)

# Display metrics in card-style containers
col1, col2, col3, col4 = st.columns(4)
col1.markdown(card_container("Production", formatted_production), unsafe_allow_html=True)
col2.markdown(card_container("Efficiency", formatted_efficiency), unsafe_allow_html=True)
col3.markdown(card_container("Converted Production", formatted_converted_production), unsafe_allow_html=True)
col4.markdown(card_container("Frame", total_frame), unsafe_allow_html=True)

# Display charts
# Your chart code here...

# Quality-wise chart
if selected_factory=="All":
    quality_df = df.groupby(df["Product Type"], as_index=False)["achieved production"].sum()
    
    try:
        fig = px.bar(quality_df, x="Product Type", y="achieved production",
                     text=['{:,.2f}'.format(x) for x in quality_df["achieved production"]],
                     template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(quality_df))
        fig.update_layout(title="Quality vs Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")

# Display mill-wise data if a factory is selected
else:
    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory
    factory_df_selected = df[df['Factory'].isin(selected_factory)]
    selected_mills_production = factory_df_selected["Mill No."].unique()
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    
    if selected_mill_number=="All":
        mill_count_df = mill_df.groupby(["Product Type"], as_index=False)["achieved production"].sum()
    else:
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["Product Type"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["Product Type"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["Product Type"], as_index=False)["achieved production"].sum()
    
    try:
        fig = px.bar(mill_count_df, x="Product Type", y="achieved production",
                     text=['{:,.2f}'.format(x) for x in mill_count_df["achieved production"]],
                     template="seaborn", width=1000, height=500,
                     color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Quality vs Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")
