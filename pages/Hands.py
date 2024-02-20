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

# Get the minimum and maximum dates from the DataFrame
min_date = hands_df["Date"].min()
max_date = hands_df["Date"].max()

# Set default values for date input widgets
default_start_date = min_date.date()
default_end_date = max_date.date()

# Display the date input widgets in two columns
col1, col2 = st.columns(2)

with col1:
    date1 = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=default_end_date)

with col2:
    date2 = st.date_input("End Date", min_value=min_date.date(), max_value=max_date.date(), value=default_end_date)

# Convert start_date and end_date to Timestamp objects
date1 = pd.Timestamp(date1)
date2 = pd.Timestamp(date2)
# date filtering section ends here



# sidebar for filtering data starts here

# st.sidebar.header("Choose your filter: ")
# # Create for Factory Name
# factory=st.sidebar.multiselect("Pick Location",
#                                hands_df["Factory"].unique(),
#                                default=hands_df["Factory"].unique()
#                                )

# if not factory:
#     hands_df2=hands_df.copy()
# else:
#     hands_df2=hands_df[hands_df["Factory"].isin(factory)]


# # Create for mill no
# millno=st.sidebar.multiselect("Choose Mill",
#                               hands_df["Mill No."].unique(),
#                               default=hands_df["Mill No."].unique()
#                               )

# if not millno:
#     hands_df3=hands_df2.copy()
# else:
#     hands_df3=hands_df2[hands_df2["Mill No."].isin(millno)]



# # Create for product type
# shift=st.sidebar.multiselect("Select Shift",
#                              hands_df["Shift"].unique(),
#                              default=hands_df["Shift"].unique()
#                              )

# if not shift:
#     hands_df4=hands_df3.copy()
# else:
#     hands_df4=hands_df3[hands_df3["Shift"].isin(shift)]

# # sidebar for filtering data ends here



# # # Filter the data based on shift, product type and mill no
# if not factory and not millno and not shift:
#     filtered_df = hands_df
# elif not factory and not millno:
#     filtered_df = hands_df[hands_df["Shift"].isin(shift)]
# elif not shift and not factory:
#     filtered_df = hands_df[hands_df["Mill No."].isin(millno)]
# elif millno and shift:
#     filtered_df = hands_df3[hands_df["Mill No."].isin(millno) & hands_df3["Shift"].isin(shift)]
# elif shift and factory:
#     filtered_df = hands_df3[hands_df["Shift"].isin(shift) & hands_df3["Factory"].isin(factory)]
# elif factory and millno:
#     filtered_df = hands_df3[hands_df["Factory"].isin(factory) & hands_df3["Mill No."].isin(millno)]
# elif shift:
#     filtered_df = hands_df3[hands_df3["Shift"].isin(shift)]
# elif millno:
#     filtered_df = hands_df3[hands_df3["Mill No."].isin(millno)]
# elif factory:
#     filtered_df = hands_df3[hands_df3["Factory"].isin(factory)]
# else:
#     filtered_df = hands_df3[hands_df3["Shift"].isin(shift) & hands_df3["Mill No."].isin(millno) & hands_df3["Factory"].isin(factory)]

# # data filtering ends here




# Define initial options for the selectboxes
all_factories = ["All"] + list(hands_df["Factory"].unique())
all_mill_nos = ["All"] + list(hands_df["Mill No."].unique())
all_buyers = ["All"] + list(hands_df["Shift"].unique())


# Create a column for filtering data
col1, col2, col3 = st.columns(3)

# Create selectboxes for filtering
with col1:
    selected_factory = st.selectbox("Factory", all_factories)

# Dynamically update options for Mill No. based on selected factory
if selected_factory != "All":
    factories_df = hands_df[hands_df["Factory"] == selected_factory]
    all_mill_nos = ["All"] + list(factories_df["Mill No."].unique())
else:
    all_mill_nos = ["All"] + list(hands_df["Mill No."].unique())

with col2:
    selected_mill_no = st.selectbox("Mill No.", all_mill_nos)

# Dynamically update options for Shift based on selected factory and mill
if selected_mill_no != "All" and selected_factory != "All":
    mill_df = hands_df[(hands_df["Mill No."] == selected_mill_no) & (hands_df["Factory"] == selected_factory)]
    shift = ["All"] + list(mill_df["Shift"].unique())
elif selected_factory != "All":
    factories_df = hands_df[hands_df["Factory"] == selected_factory]
    shift = ["All"] + list(factories_df["Shift"].unique())
else:
    shift = ["All"] + list(hands_df["Shift"].unique())

with col3:
    selected_Shift = st.selectbox("Shift", shift)



st.markdown("")


# Filter the data based on selected filters
filtered_df = hands_df.copy()
if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]
if selected_mill_no != "All":
    filtered_df = filtered_df[filtered_df["Mill No."] == selected_mill_no]
if selected_Shift != "All":
    filtered_df = filtered_df[filtered_df["Shift"] == selected_Shift]


# groupby shift for data visualization
factory_df=filtered_df.groupby(filtered_df["Factory"], as_index=False)["Hands"].sum()
sectionwise_df=filtered_df.groupby(filtered_df["Section"], as_index=False)["Hands Per Ton"].sum()
millwise_hands=filtered_df.groupby(filtered_df["Mill No."], as_index=False)["Hands"].sum()
factory_df_hands_per_ton=filtered_df.groupby(filtered_df["Factory"], as_index=False)["Hands Per Ton"].sum()
shift_wise_hands_per_ton=filtered_df.groupby(filtered_df["Shift"],as_index=False)["Hands Per Ton"].sum()


# shift for text columns
col1,col2,col3=st.columns((1,1,2))

total_hands=filtered_df["Hands"].sum()
hands_per_ton=filtered_df["Hands Per Ton"].sum()



with col1:
        formatted_total_hands="{:.2f}".format(total_hands)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Total Hands</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_total_hands}</p>'
        st.markdown(value,unsafe_allow_html=True)

with col2:

        formatted_total_hands="{:.2f}".format(hands_per_ton)
        original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Hands Per Ton</p>'
        st.markdown(original_title,unsafe_allow_html=True)
        value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;text-align:center">{formatted_total_hands}</p>'
        st.markdown(value,unsafe_allow_html=True)

with col3:
    # Define the list of selected departments
    selected_departments = ["Spreader", "Breaker", "Drawing", "Spinning", "Finisher", "Roll Winding", "Precision Winding"]
    selected_departments_mechanical = ["Mechanical"]
    selected_departments_quality = ["Quality"]
    selected_departments_production_general = ["Production General"]

    # Filter the DataFrame to include only the selected departments
    selected_df = filtered_df[filtered_df["Section"].isin(selected_departments)]

    # Group by "Section" (department) and sum the values of "Hands" for each department
    production_department = selected_df["Hands"].sum()
    formatted_production_department="{:.2f}".format(production_department)


    # Filter the DataFrame to include only the mechanical department
    selected_df_mechanical = filtered_df[filtered_df["Section"].isin(selected_departments_mechanical)]
    mechanical_dept = selected_df_mechanical["Hands"].sum()
    formatted_mechanical_department="{:.2f}".format(mechanical_dept)

    # Filter the DataFrame to include only the quality department
    selected_df_quality = filtered_df[filtered_df["Section"].isin(selected_departments_quality)]
    quality_dept = selected_df_quality["Hands"].sum()
    formatted_quality_department="{:.2f}".format(quality_dept)
    

    # Filter the DataFrame to include only the production general department
    selected_df_production_general = filtered_df[filtered_df["Section"].isin(selected_departments_production_general)]
    production_general_dept = selected_df_production_general["Hands"].sum()


    original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Hands </p>'
    st.markdown(original_title,unsafe_allow_html=True)
        # value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 18px; font-weight:bold;">{formatted_actual_production}</p>'
            # st.markdown(value,unsafe_allow_html=True)
            # st.markdown("")
            # st.markdown("")
            # st.markdown("")


    col1_prod, col1_mech,col1_quality =st.columns((3))
    
    with col1_prod:
                original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center;">Production</p>'
                st.markdown(original_title,unsafe_allow_html=True)

                value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center;">{formatted_production_department}</p>'
                st.markdown(value,unsafe_allow_html=True)

                st.markdown("")
                st.markdown("")
                st.markdown("")
            

    with col1_mech:
                original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Mechanical</p>'
                st.markdown(original_title,unsafe_allow_html=True)

                value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_mechanical_department}</p>'
                st.markdown(value,unsafe_allow_html=True)

                st.markdown("")
                st.markdown("")
                st.markdown("")
        
    with col1_quality:
                original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 15px; font-weight:bold;text-align:center">Quality</p>'
                st.markdown(original_title,unsafe_allow_html=True)

                value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 15px; font-weight:bold;text-align:center"">{formatted_quality_department}</p>'
                st.markdown(value,unsafe_allow_html=True)

                st.markdown("")
                st.markdown("")
                st.markdown("")

st.markdown("")
    
# else:
#     with col1:
#         formatted_total_hands="{:.2f}".format(total_hands)
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Total Hands</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 20px; font-weight:bold;">{formatted_total_hands}</p>'
#         st.markdown(value,unsafe_allow_html=True)
       

#     with col2:
#         formatted_total_hands="{:.2f}".format(hands_per_ton)
#         original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 20px; font-weight:bold;">Hands Per Ton</p>'
#         st.markdown(original_title,unsafe_allow_html=True)
#         value = f'<p style="font-family:Arial-Black; color:#AC3E31; font-size: 20px; font-weight:bold;">{formatted_total_hands}</p>'
#         st.markdown(value,unsafe_allow_html=True)
       

# end section for text columns



# starts section for charts
col1,col2=st.columns((2))
with col1:
    try:
        # original_title = '<p style="font-family:Arial-Black; color:Black; font-size: 18px; font-weight:bold;text-align:center">Factory Wise Hands</p>'
        # st.markdown(original_title,unsafe_allow_html=True)
    
        fig=px.bar(factory_df,x="Factory",y="Hands",text=['{:,.2f}'.format(x) for x in factory_df["Hands"]],
                    template = "seaborn",height=350,width=350)
        fig.update_layout(title="Factory Wise Hands")
    
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

col1,col2=st.columns(2)
with col1:
     
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

with col2:
    

    # hands_per_ton_df = sectionwise_df.groupby(sectionwise_df["Section"], as_index=False)["Hands Per Ton"].sum()
   
    try:
            # Create a bar chart for production by factory
            fig = px.bar(sectionwise_df, x="Section", y="Hands Per Ton", text=['{:,.2f}'.format(x) for x in sectionwise_df["Hands Per Ton"]],
                        template="seaborn", width=350, height=350, color_discrete_sequence=[" #488A99"] * len(sectionwise_df))
            fig.update_layout(title="Production by Factory")
            st.plotly_chart(fig, use_container_width=True)

    except IndexError:
            st.warning("No data found for the specified filter.")