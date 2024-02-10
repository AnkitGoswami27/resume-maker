import streamlit as st
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from streamlit_lottie import st_lottie
# Streamlit App
st.title("Job Alert System")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/3dc376e2-7e55-4eef-9080-5cd10e363899/KdY8BfjEwu.json")

# User Input
with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
      email = st.text_input("Enter your email:")
      resume = st.file_uploader("Upload your resume (PDF only):", type="pdf")
      field_of_study = st.text_input("Enter your field of study:")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# API Configuration (Replace with your actual API details)
api_key = "85d96dc605msh30c39a803af3cebp19cccajsnf880e7cb16f6"
api_endpoint = "https://jobs-api14.p.rapidapi.com/list"

# Function to fetch job alerts from the API
def fetch_job_alerts(field_of_study):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jobs-api14.p.rapidapi.com"
    }
    params = {
        "query": field_of_study,
        "location": "India",
        "distance": "1.0",
        "language": "en_GB",
        "remoteOnly": "false",
        "datePosted": "month",
        "emplyomentTypes": "fulltime;parttime;intern;contractor",
        "index": "0"
    }
    
    response = requests.get(api_endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json().get("jobs", [])
    else:
        return None

# Email Button
if st.button("Send Job Alerts"):
    # Check if email and resume are provided
    if email and resume and field_of_study:
        try:
            # Email Configuration
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "ankit.op113@gmail.com"
            sender_password = "ugwa pybc oodl wmnh"

            # Connect to SMTP Server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Create Message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = 'Job Alerts for ' + field_of_study

            # Fetch job alerts when the button is clicked
            job_alerts = fetch_job_alerts(field_of_study)

            # Attach Resume
            resume_data = resume.read()
            resume_attachment = MIMEApplication(resume_data, _subtype="pdf")
            resume_attachment.add_header('Content-Disposition', 'attachment', filename='resume.pdf')
            msg.attach(resume_attachment)

            # Compose Email Body
            body = f"Hello,\n\nHere are the latest job alerts for your field of study ({field_of_study}):"
            for job in job_alerts:
                body += f"\n\n- {job['title']} at {job['company']} in {job['location']}"

            msg.attach(MIMEText(body, 'plain'))

            # Send Email
            server.sendmail(sender_email, email, msg.as_string())

            # Close SMTP Connection
            server.quit()

            st.success("Job alerts sent successfully!")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please provide email, resume, and field of study.")
