import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Access API keys from secrets
firebase_config = {
    "type": "service_account",
    "project_id": "heatloss-69a51",
    "private_key_id": st.secrets["fb_private_key_id"],
    "private_key": st.secrets["fb_private_key"],
    "client_email": st.secrets["fb_client_email"],
    "client_id": st.secrets["fb_client_id"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-d8rr6%40heatloss-69a51.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}


cred = credentials.Certificate(firebase_config)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


def app():
    
    if 'user' not in st.session_state:
            st.session_state.user = None
    
    if 'userid' not in st.session_state:
            st.session_state.userid = None
    if 'usermail' not in st.session_state:
            st.session_state.usermail = None
    if 'username' not in st.session_state:
            st.session_state.username = None

    st.title("Login")

    def f():
        try:
            user= auth.get_user_by_email(email)
            
            if user.email_verified:
            
                userid = user.uid
                usermail = user.email
                username = user.display_name
                st.session_state.user = user
                st.session_state.userid = userid
                st.session_state.usermail = usermail
                st.session_state.username = username
            
                st.success('Login Successful')
            else:
                st.warning("Email non verificata. Controlla la tua casella di posta per il link di verifica.")
                
        except Exception as e:
            st.warning(e)
    

    # Function to log out
    def logout():
        st.session_state['user'] = None
        # Additional logout steps if needed (e.g., clearing cookies)
        st.success("You have been logged out.")


    email= st.text_input("Enter your email")
    password= st.text_input("Enter your password", type= 'password')

    st.button('Login', on_click= f)

    if st.session_state['user'] != None:
        st.sidebar.write(f'Welcome *{st.session_state["username"]}*')
        #st.sidebar.write(f'user id: *{st.session_state["userid"]}*')
        st.sidebar.write(f'email: *{st.session_state["usermail"]}*')

        st.sidebar.button("Logout", on_click= logout)
    
    
    
        
        
        
    





