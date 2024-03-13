import streamlit as st
import streamlit_authenticator as stauth
import pyrebase
import sys
sys.path.append("pages")





firebaseConfig = {
    'apiKey': "AIzaSyARU9qbSpQVQoa5P07KKnfSVGJmARz-8H0",
    'authDomain': "user-authentication-cc9fc.firebaseapp.com",
    'projectId': "user-authentication-cc9fc",
    'databaseURL':"https://user-authentication-cc9fc-default-rtdb.firebaseio.com/",
    'storageBucket': "user-authentication-cc9fc.appspot.com",
    'messagingSenderId': "465376937159",
    'appId': "1:465376937159:web:9105546dc67d1590332ae2",
    'measurementId': "G-NX2L9BT730"
  }

# firebase authentication

firebase=pyrebase.initialize_app(firebaseConfig)

# Authentication state management (using Session State)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["user"] = None

auth=firebase.auth()

# database
db=firebase.database()
storage=firebase.storage()

# Authentication

# st.subheader("Login/Signup")

# choice = st.selectbox("Choose an action", ['Login', 'Signup'])

# email = st.text_input("Please enter email address")
# password = st.text_input("Please enter password", type="password")



# if choice =="Signup":
#     submit=st.button("Create my account")

#     if submit:
#         user=auth.create_user_with_email_and_password(email,password)
#         st.success("Your account is created successfully")
#         st.balloons()

#         # SIgn In
#         # user=auth.sign_in_with_email_and_password(email,password)
#         # db.child(user['localId']).child("ID").set(user['localId'])
#         # st.title("Welcome")

# else:
#     submit=st.button("Log In")
#     if submit:
#         # SIgn In
#         user=auth.sign_in_with_email_and_password(email,password)
#         db.child(user['localId']).child("ID").set(user['localId'])
#         st.title("Welcome")




def login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.session_state["authenticated"] = True
        st.session_state["user"] = user["idToken"]
        st.success("Login successful!")
        return True
    except Exception as e:
        st.error(f"Login failed: {e}")
        return False

def signup(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.session_state["authenticated"] = True
        st.session_state["user"] = user["idToken"]
        st.success("Signup successful!")
        return True
    except Exception as e:
        st.error(f"Signup failed: {e}")
        return False

def logout():
    st.session_state["authenticated"] = False
    st.session_state["user"] = None
    st.success("Logout successful!")


def handle_login_logout():
    if not st.session_state["authenticated"]:
        with st.form("Login/Signup"):
            choice = st.selectbox("Choose an action", ['Login', 'Signup'])
            email = st.text_input("Please enter email address")
            password = st.text_input("Please enter password", type="password")
            submit_button = st.form_submit_button("Submit")  # Added the missing button

            if submit_button:
                if choice == "Login":
                    if login(email, password):
                        # Hide navigation bar after successful login (experimental)
                       st.success("login Successful!")
                    else:
                        st.warning("Unauthorized Credential")
                else:  # Signup
                    if signup(email, password):
                        st.success("Signup successful!")
                        # Hide navigation bar after successful signup (optional)
                        # st.experimental_hide_streamlit_menu()  # Uncomment if desired

    else:  # User is authenticated
        st.warning("Undefined Credentials!")






def main():
    handle_login_logout()


    if st.session_state["authenticated"]:
        from pages.Production_Dashboard import production_dashboard
        from pages.Production_Details import Peroduction_details
        from pages.Stock import Stock
        from pages.Hands import Hands
        from pages.file_uploader import file_uploader


        






if __name__ == "__main__":
    main()