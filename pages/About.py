import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://lottie.host/1af775d8-7e86-4149-9bca-2d1eeb69842a/SQtcahRxTS.json")

def about_us():
    st.title("About Us")
    with st.container():
        left_column,right_column=st.columns(2)
        with left_column:
         st.write(
        """
        Welcome to Our Job Portal! 🌟

        At Our Job Portal, we are passionate about connecting talented individuals with exciting job opportunities. Our mission is to make the job search process easier and more efficient for both employers and job seekers.

        ![Team](https://example.com/team_photo.jpg)
        *Our Amazing Team at Our Job Portal*

       """
    )
        with right_column:
            st_lottie(lottie_coding,height=300,key="coding")
           

if __name__ == "__main__":
    about_us()

# Adding Lottie Animation




st.markdown("""
            
            ## Team Members :-
            1. ANKIT GOSWAMI(2201431530008)
            2. AMAN SINGH(2201431530006)
            3. HIMANSHU RAUTELA (2201431530025)
            
            """)
