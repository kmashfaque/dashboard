import streamlit as st
import plotly.express as px  # pip install plotly-express
import pandas as pd
import base64  # Standard Python Module
import xlrd




st.subheader("Dataset")

# File uploader
data_files = st.file_uploader("Upload Spreadsheet File", type=['csv', 'xlsx','xlsm'], accept_multiple_files=True)

if data_files is not None:
    if st.button("Process"):
        st.markdown("-------")
        for data_file in data_files:
            st.write(f"File Name: {data_file.name}")

            stock_entry_file=["stock_entry_JJMLF.xlsm","stock_entry_JJMLN.xlsm","stock_entry_SJIL.xlsm"]
            hands_entry_file=["Hands Per Ton - JJMLF.xlsm","Hands Per Ton - JJMLN.xlsm","Hands Per Ton - SJIL.xlsm"]


            if data_file.name in stock_entry_file:
                try:
                    if data_file.type == 'application/vnd.ms-excel':
                        # Read Excel file using openpyxl engine
                        df = pd.read_excel(data_file, engine="openpyxl")
                        st.write(df)
                    else:
                        df = pd.read_excel(data_file,sheet_name="Daily Update",skiprows=8)
                        st.write(df)
                except Exception as e:
                    st.error(f"An error occurred while processing {data_file.name}: {e}")
            

            elif data_file.name in hands_entry_file:
                try:
                    if data_file.type == 'application/vnd.ms-excel':
                        # Read Excel file using openpyxl engine
                        df = pd.read_excel(data_file, engine="openpyxl")
                        st.write(df)
                    else:
                        df = pd.read_excel(data_file,sheet_name="Daily Update",skiprows=10)
                        st.write(df)
                except Exception as e:
                    st.error(f"An error occurred while processing {data_file.name}: {e}")

            
            else:
                    try:
                        if data_file.type == 'application/vnd.ms-excel':
                            # Read Excel file using openpyxl engine
                            df = pd.read_excel(data_file, engine="openpyxl")
                            st.write(df)
                        else:
                            df = pd.read_excel(data_file,sheet_name="Summary",skiprows=15)
                            st.write(df)
                    except Exception as e:
                        st.error(f"An error occurred while processing {data_file.name}: {e}")






