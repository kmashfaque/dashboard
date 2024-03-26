import streamlit as st
import plotly.express as px  # pip install plotly-express
import pandas as pd
import base64  # Standard Python Module
import xlrd
import os


# def file_uploader():
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
            juteissue_entry_file=["Jute Issue Format_JJMLF.xlsm","Jute Issue Format_JJMLN.xlsm","Jute Issue Format_SJIL.xlsm"]




        if data_file.name in stock_entry_file:
            stock_dataframe = []

            try:
                if data_file.type == 'application/vnd.ms-excel':
                    # Read Excel file using openpyxl engine
                    df = pd.read_excel(data_file, engine="openpyxl")
                else:
                    df = pd.read_excel(data_file, sheet_name="Daily Update", skiprows=8)
                stock_dataframe.append(df)

                merged_df = pd.concat(stock_dataframe)

                file_path = "Stocks - Copy.xlsx"

                # Check if the file exists
                if os.path.exists(file_path):
                    existing_data = pd.read_excel(file_path)

                    # Get the last appended data
                    last_appended_data = existing_data.tail(len(merged_df))

                    # Filter out rows present in both the last appended data and the new data
                    new_data = merged_df[~(merged_df.set_index(["Date", "Factory", "Mill No."]).index.isin(last_appended_data.set_index(["Date", "Factory", "Mill No."]).index))]
                    print(new_data)
                    if len(new_data) > 0:
                        # Append only the changed rows from the new data to the existing data
                        updated_data = pd.concat([existing_data, new_data], ignore_index=True)

                        # Convert only the columns with integer dtype
                        for column in existing_data.select_dtypes(include=["int"]).columns:
                            updated_data[column] = updated_data[column].astype(existing_data[column].dtype, errors="ignore")

                        updated_data.to_excel(file_path, index=False)
                        print("New data appended.")
                    else:
                        print("No new data to append.")
                else:
                    # If the file doesn't exist, create it with the initial data
                    merged_df.to_excel(file_path, index=False)
                    print("New file created with initial data.")
            except Exception as e:
                print("Error occurred:", str(e))
                                                    



            except Exception as e:
                st.error(f"An error occurred while processing {data_file.name}: {e}")
                

        elif data_file.name in hands_entry_file:
                    hands_dataframe=[]
                    try:
                        if data_file.type == 'application/vnd.ms-excel':
                            # Read Excel file using openpyxl engine
                            df = pd.read_excel(data_file, engine="openpyxl")
                            # st.write(df)
                        else:
                            df = pd.read_excel(data_file,sheet_name="Daily Update",skiprows=10)
                            # st.write(df)
                            hands_dataframe.append(df)
                        merged_df=pd.concat(hands_dataframe)
                        
                        file_path="HandsPerTon - Copy.xlsx"

                        # Check if the file exists
                        if os.path.exists(file_path):
                            existing_data = pd.read_excel(file_path)

                            # Get the last appended data
                            last_appended_data = existing_data.tail(len(merged_df))

                            # Filter out rows present in both the last appended data and the new data
                            new_data = merged_df[~(merged_df.set_index(["Date", "Factory","Mill No."]).index.isin(last_appended_data.set_index(["Date", "Factory","Mill No."]).index))]

                            if len(new_data) > 0:
                                # Append only the changed rows from the new data to the existing data
                                updated_data = pd.concat([existing_data, new_data], ignore_index=True)

                                # Convert only the columns with integer dtype
                                for column in existing_data.select_dtypes(include=["int"]).columns:
                                    updated_data[column] = updated_data[column].astype(existing_data[column].dtype, errors="ignore")

                                updated_data.to_excel(file_path, index=False)
                                print("New data appended.")
                            else:
                                print("No new data to append.")
                        else:
                            # If the file doesn't exist, create it with the initial data
                            merged_df.to_excel(file_path, index=False)
                            print("New file created with initial data.")

                    except Exception as e:
                        st.error(f"An error occurred while processing {data_file.name}: {e}")

        elif data_file.name in juteissue_entry_file:
                    hands_dataframe=[]
                    try:
                        if data_file.type == 'application/vnd.ms-excel':
                            # Read Excel file using openpyxl engine
                            df = pd.read_excel(data_file, engine="openpyxl")
                            # st.write(df)
                        else:
                            df = pd.read_excel(data_file,sheet_name="Summary",skiprows=10)
                            # st.write(df)
                            hands_dataframe.append(df)
                        merged_df=pd.concat(hands_dataframe)
                        
                        file_path="Juteissue - Copy.xlsx"

                        # Check if the file exists
                        if os.path.exists(file_path):
                            existing_data = pd.read_excel(file_path)

                            # Get the last appended data
                            last_appended_data = existing_data.tail(len(merged_df))

                            # Filter out rows present in both the last appended data and the new data
                            new_data = merged_df[~(merged_df.set_index(["Date", "Factory","Mill No."]).index.isin(last_appended_data.set_index(["Date", "Factory","Mill No."]).index))]

                            if len(new_data) > 0:
                                # Append only the changed rows from the new data to the existing data
                                updated_data = pd.concat([existing_data, new_data], ignore_index=True)

                                # Convert only the columns with integer dtype
                                for column in existing_data.select_dtypes(include=["int"]).columns:
                                    updated_data[column] = updated_data[column].astype(existing_data[column].dtype, errors="ignore")

                                updated_data.to_excel(file_path, index=False)
                                print("New data appended.")
                            else:
                                print("No new data to append.")
                        else:
                            # If the file doesn't exist, create it with the initial data
                            merged_df.to_excel(file_path, index=False)
                            print("New file created with initial data.")

                    except Exception as e:
                        st.error(f"An error occurred while processing {data_file.name}: {e}")

        else:
                        spng_dataframe=[]
                        try:
                            if data_file.type == 'application/vnd.ms-excel':
                                # Read Excel file using openpyxl engine
                                df = pd.read_excel(data_file, engine="openpyxl")
                                # st.write(df)

                            else:
                                df = pd.read_excel(data_file,sheet_name="Summary",skiprows=15)
                                # st.write(df)
                                spng_dataframe.append(df)
                            
                            merged_df=pd.concat(spng_dataframe)

                            file_path="production - Copy.xlsx"

                            # Check if the file exists
                            if os.path.exists(file_path):
                                existing_data = pd.read_excel(file_path)

                                # Get the last appended data 
                                last_appended_data = existing_data.tail(len(merged_df))

                                # Filter out rows present in both the last appended data and the new data
                                new_data = merged_df[~(merged_df.set_index(["Date", "Factory","Mill No."]).index.isin(last_appended_data.set_index(["Date", "Factory","Mill No."]).index))]

                                if len(new_data) > 0:
                                    # Append only the changed rows from the new data to the existing data
                                    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

                                    # Convert only the columns with integer dtype
                                    for column in existing_data.select_dtypes(include=["int"]).columns:
                                        updated_data[column] = updated_data[column].astype(existing_data[column].dtype, errors="ignore")

                                    updated_data.to_excel(file_path, index=False)
                                    print("New data appended.")
                                else:
                                    print("No new data to append.")
                            else:
                                # If the file doesn't exist, create it with the initial data
                                merged_df.to_excel(file_path, index=False)
                                print("New file created with initial data.")                        

                        except Exception as e:
                            st.error(f"An error occurred while processing {data_file.name}: {e}")









