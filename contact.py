import streamlit as st

def app():
    st.header(":mailbox: Get in touch with me!")

    contact_form = """
    <form action="https://formsubmit.co/solvingvv@gmail.com" method="POST">
        <input type="text" name="name" placeholder= "Enter Your name" required>
        <input type="email" name="email" placeholder= "Enter Your email" required>
        <textarea name="message" placeholder="Enter Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """


    st.markdown(contact_form, unsafe_allow_html= True)

    #use local_css File

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

    local_css("styles/style.css")

