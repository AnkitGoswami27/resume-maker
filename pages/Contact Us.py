import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://lottie.host/27e20d77-61e2-44e9-ae7b-28fe4446f592/5hkUMMYTn8.json")

def contact_form():
    st.subheader("Contact Us")
    
    # Input fields for name, email, and message
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")

    # Submit button
    if st.button("Submit"):
        st.success("Message Sent!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Message: {message}")
        st.balloons()

# Streamlit App
st.title("Contact Form ")

# Display the contact form
with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
     contact_form()
    with right_column:
       st_lottie(lottie_coding,height=300,key="coding")
       

