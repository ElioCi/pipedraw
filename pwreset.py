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

def app():

    def send_reset_email(to_email, reset_link):
        from_email = "solvingvv@gmail.com"  # Your email address
        from_password = "ocfa uypo udbb hsfy"  # Your email password
        subject = "Reset Your Password"
        body = f"Click the link to reset your password: {reset_link}"
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Your SMTP server
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            st.error(f"Error sending email: {e}")
            return False

    st.title("Reset Password")

    email = st.text_input("Enter your email address")

    if st.button("Send Password Reset Email"):
        if email:
            try:
                # Generate the password reset link
                reset_link = auth.generate_password_reset_link(email)
                
                # Send the link via email (requires setting up an email service)
                if send_reset_email(email, reset_link):
                    st.success("Password reset email sent! Please check your inbox.")
                else:
                    st.error("Failed to send password reset email. Please try again later.")
            except firebase_admin.auth.UserNotFoundError:
                st.error("No user found with this email address.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter your email address.")




