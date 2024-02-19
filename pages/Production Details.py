
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib as mult
import plotly.graph_objs as go


warnings.filterwarnings("ignore")

st.set_page_config(page_title="Over All Production!!", page_icon=":bar_chart:", layout="wide")


st.title(" :bar_chart: Production Details Dashboard")
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

# Filter mill numbers based on the selected factory
if selected_factory == "All":
    filtered_mill_numbers = df["Mill No."].unique()
else:
    filtered_mill_numbers = df[df["Factory"] == selected_factory]["Mill No."].unique()

    # Create a selectbox for Mill Name
    selected_mill_number = st.sidebar.selectbox("Pick Mill No.",
                                                ["All"] + list(filtered_mill_numbers),
                                                index=0)

# Start sections for charts
col1, col2, col3 = st.columns((3))

# Display factory-wise charts
if selected_factory=="All":
    factory_df = df.groupby(df["Factory"], as_index=False)["actual production"].sum()
    efficiency_df = df.groupby(df["Factory"], as_index=False)["Efficiency"].mean()
    ply_df=df.groupby(df["Ply"],as_index=False)["actual production"].sum()
   
    with col1:
        try:
            # Create a bar chart for production by factory
            fig = px.bar(factory_df, x="Factory", y="actual production", text=['{:,.2f}'.format(x) for x in factory_df["actual production"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(factory_df))
            fig.update_layout(title="Production ")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")

    with col2:
        try:
            # Create a bar chart for efficiency by factory
            fig = px.bar(efficiency_df, x="Factory", y="Efficiency", text=['{:,.2f}'.format(x) for x in efficiency_df["Efficiency"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #1C4E80"] * len(efficiency_df))
            fig.update_layout(title="Efficiency ")
            st.plotly_chart(fig, use_container_width=True)

        except IndexError:
            st.warning("No data found for the specified filter.")
    

    with col3:
        try:
            # Create a bar chart for production by factory
            fig = px.bar(ply_df, x="Ply", y="actual production", text=['{:,.2f}'.format(x) for x in ply_df["actual production"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(ply_df))
            fig.update_layout(title="Ply")
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
        mill_ply_df = factory_df_selected.groupby(["Ply"], as_index=False)["actual production"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["Ply"].unique()
        mill_df_ply = mill_df_selected[mill_df_selected["Ply"].isin(selected_mills)]
        mill_ply_df = mill_df_ply.groupby(["Ply"], as_index=False)["actual production"].sum()

   
    
    mill_production_df = mill_df.groupby(["Mill No."], as_index=False)["actual production"].sum()
    mill_efficiency_df = mill_df.groupby(["Mill No."], as_index=False)["Efficiency"].mean()

  


    with col1:
        try:
            # Create a bar chart for production by mill number
            fig = px.bar(mill_production_df, x="Mill No.", y="actual production",
                         text=['{:,.2f}'.format(x) for x in mill_production_df["actual production"]],
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
            fig = px.bar(mill_ply_df, x="Ply", y="actual production", 
                         text=['{:,.2f}'.format(x) for x in mill_ply_df["actual production"]],
                         template="seaborn", width=700, height=350,
                         color_discrete_sequence=[" #488A99"] * len(mill_ply_df))
            fig.update_layout(title="Ply")
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

  
    # new


    selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

    # Filter the DataFrame based on the selected factories
    factory_df_selected = df[df['Factory'].isin(selected_factory)]

    # Extract unique mill numbers from the selected factory DataFrame
    selected_mills_production = factory_df_selected["Mill No."].unique()

    # Filter the DataFrame to include only the selected mills
    mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]
    

    if selected_mill_number=="All":
        mill_count_df = mill_df.groupby(["count"], as_index=False)["actual production"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["count"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["count"], as_index=False)["actual production"].sum()

   
    

  
    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_count_df, x="count", y="actual production",
        text=['{:,.2f}'.format(x) for x in mill_count_df["actual production"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Countwise Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")

   




# frame vs count chart

if selected_factory=="All":
    count_df = df.groupby(df["count"], as_index=False)["Frame"].sum()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(count_df, x="count", y="Frame", text=['{:,.2f}'.format(x) for x in count_df["Frame"]],
        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
        fig.update_layout(title="Frame vs Count")
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
        mill_count_df = mill_df.groupby(["count"], as_index=False)["Frame"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["count"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["count"], as_index=False)["Frame"].sum()

   
    

  
    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_count_df, x="count", y="Frame",
        text=['{:,.2f}'.format(x) for x in mill_count_df["Frame"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Frame vs Count")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")


# efficiency vs count chart

if selected_factory=="All":
    count_df = df.groupby(df["count"], as_index=False)["Efficiency"].mean()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(count_df, x="count", y="Efficiency", text=['{:,.2f}'.format(x) for x in count_df["Efficiency"]],
        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(count_df))
        fig.update_layout(title="Efficiency vs Count")
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
        mill_count_df = mill_df.groupby(["count"], as_index=False)["Efficiency"].mean()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["count"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["count"], as_index=False)["Efficiency"].mean()

  
    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_count_df, x="count", y="Efficiency",
        text=['{:,.2f}'.format(x) for x in mill_count_df["Efficiency"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Efficiency vs Count")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")





# Quality vs production chart

if selected_factory=="All":
    quality_df = df.groupby(df["Product Type"], as_index=False)["actual production"].sum()
    
    try:
        # Create a bar chart for production by factory
        fig = px.bar(quality_df, x="Product Type", y="actual production", text=['{:,.2f}'.format(x) for x in quality_df["actual production"]],
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
        mill_count_df = mill_df.groupby(["Product Type"], as_index=False)["actual production"].sum()

    else:

        # Group by both mill number to get production data for ply
        selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
        mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
        selected_mills = mill_df_selected["Product Type"].unique()
        mill_df_count = mill_df_selected[mill_df_selected["Product Type"].isin(selected_mills)]
        mill_count_df = mill_df_count.groupby(["Product Type"], as_index=False)["actual production"].sum()

    try:
        # Create a bar chart for production by mill number
        fig = px.bar(mill_count_df, x="Product Type", y="actual production",
        text=['{:,.2f}'.format(x) for x in mill_count_df["actual production"]],
        template="seaborn", width=1000, height=500,
        color_discrete_sequence=[" #488A99"] * len(mill_count_df))
        fig.update_layout(title="Quality vs Production")
        st.plotly_chart(fig, use_container_width=True)

    except IndexError:
        st.warning("No data found for the specified filter.")




# frame with count vs production 
        
# if selected_factory == "All":
#     count_df = df.groupby(df["count"], as_index=False)["actual production"].sum()
    
#     try:
#         # Create a bar chart for production by factory
#         fig = px.bar(count_df, x="count", y="actual production", 
#                      text=['{:,.2f}'.format(x) for x in count_df["actual production"]],
#                      template="seaborn", width=1000, height=500, 
#                      color_discrete_sequence=[" #488A99"] * len(count_df))
#         fig.update_layout(title="Countwise Production")
        
#         # Add scatter plot for frame data
#         frame_data = df.groupby("count", as_index=False)["Frame"].sum()
#         fig.add_trace(go.Scatter(x=frame_data["count"], y=frame_data["Frame"], 
#                                  mode="markers", name="Frame Data", marker=dict(color="red", size=10)))

#         # Add frame data as text annotations
#         for i, row in frame_data.iterrows():
#             fig.add_annotation(x=row["count"], y=row["Frame"], text=f'{row["Frame"]:.2f}',
#                                font=dict(color='white', size=12), showarrow=True, arrowhead=1)

#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#         st.warning("No data found for the specified filter.")

# # Display mill-wise data if a factory is selected
# else:
#     selected_factory = [selected_factory] if isinstance(selected_factory, str) else selected_factory

#     # Filter the DataFrame based on the selected factories
#     factory_df_selected = df[df['Factory'].isin(selected_factory)]

#     # Extract unique mill numbers from the selected factory DataFrame
#     selected_mills_production = factory_df_selected["Mill No."].unique()

#     # Filter the DataFrame to include only the selected mills
#     mill_df = factory_df_selected[factory_df_selected["Mill No."].isin(selected_mills_production)]

#     if selected_mill_number == "All":
#         mill_count_df = mill_df.groupby(["count"], as_index=False)["actual production"].sum()
#     else:
#         # Group by both mill number to get production data for ply
#         selected_mill_number = [selected_mill_number] if isinstance(selected_mill_number, str) else selected_mill_number
#         mill_df_selected = factory_df_selected[factory_df_selected['Mill No.'].isin(selected_mill_number)]
#         selected_mills = mill_df_selected["count"].unique()
#         mill_df_count = mill_df_selected[mill_df_selected["count"].isin(selected_mills)]
#         mill_count_df = mill_df_count.groupby(["count"], as_index=False)["actual production"].sum()

#     try:
#         # Create a bar chart for production by mill number
#         fig = px.bar(mill_count_df, x="count", y="actual production",
#                      text=['{:,.2f}'.format(x) for x in mill_count_df["actual production"]],
#                      template="seaborn", width=1000, height=500,
#                      color_discrete_sequence=[" #488A99"] * len(mill_count_df))
#         fig.update_layout(title="Countwise Production")

#         # Add scatter plot for frame data
#         frame_data = mill_df.groupby("count", as_index=False)["Frame"].sum()
#         fig.add_trace(go.Scatter(x=frame_data["count"], y=frame_data["Frame"],
#                                  mode="markers", name="Frame Data", marker=dict(color="red", size=10)))

#         # Add frame data as text annotations
#         for i, row in frame_data.iterrows():
#             fig.add_annotation(x=row["count"], y=row["Frame"], text=f'{row["Frame"]:.2f}',
#                                font=dict(color='white', size=12), showarrow=True, arrowhead=1)

#         st.plotly_chart(fig, use_container_width=True)

#     except IndexError:
#         st.warning("No data found for the specified filter.")
