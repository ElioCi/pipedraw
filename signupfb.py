import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

#Authentication
#Signup

def app():
    st.title("Signup")

    def send_verification_email(to_email, verification_link):
        from_email = "solvingvv@gmail.com"  # Sostituisci con il tuo indirizzo email
        from_password = "ocfa uypo udbb hsfy"  # Sostituisci con la tua password email
        subject = "Verify your email"
        body = f"Please verify your email by clicking the following link: {verification_link}"
    
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Usa il tuo SMTP server
            server.starttls()
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            return True
        except Exception as e:
            st.error(f"Errore nell'invio dell'email: {e}")
            return False        
                
       
    
    def r():    #registrazione utente
            
        if email and password and username:
            try:
                # Crea un nuovo utente con email e password
                user = auth.create_user(
                    email=email,
                    password=password,
                    display_name=username,
                    email_verified=False,  # L'email non è verificata al momento della creazione
                )
                
                # Genera il link di verifica email
                verification_link = auth.generate_email_verification_link(email)
                
                # Invia il link via email
                if send_verification_email(email, verification_link):
                    st.success("Registration completed! Check your email to activate your account.")
                    st.balloons()
                else:
                    st.error("Errore nell'invio dell'email di verifica. Per favore, riprova.")
            except Exception as e:
                st.error(f"Errore nella registrazione: {e}")
        else:
            st.warning("Per favore, completa tutti i campi.")
                

      
    email= st.text_input("Enter your email")
    password= st.text_input("Enter your password", type= 'password')
    username= st.text_input("Enter your username")

    st.button('create my account', on_click= r)
            





