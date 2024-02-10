from fpdf import FPDF
import streamlit as st

# Function to create a styled PDF resume
def create_resume_pdf(first_name, last_name, phone, address, college_name, degree, field_of_study, skills, positions, responsibilities, projects, achievements, description):
    pdf = FPDF()
    pdf.add_page()

    # Set font and colors
    pdf.set_font("Arial", style='B', size=16)
    pdf.set_fill_color(100, 149, 237)  # Cornflower Blue
    pdf.set_text_color(255, 255, 255)  # White

    # Header with user description
    pdf.cell(200, 10, txt=f"{first_name} {last_name}", ln=True, align='C', fill=True)
    
    # Set font for address and phone to match the description font
    pdf.set_font("Arial", size=10)
    
    pdf.cell(200, 10, txt=f"{phone} | {address}", ln=True, align='C', fill=True)
    
    # Description in smaller font
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.ln(3)  # Add a bit of space before the description
    pdf.multi_cell(0, 8, txt=description)
   
    # Reset colors for the rest of the resume
    pdf.set_fill_color(255, 255, 255)  # White
    pdf.set_text_color(0, 0, 0)  # Black
    
    # Qualifications
    pdf.ln(1)  # Add spacing before the Qualifications section
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Qualifications", ln=True)
    # Line separator after Personal Details
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"College: {college_name}", ln=True)
    pdf.cell(200, 10, txt=f"Degree: {degree}", ln=True)
    pdf.cell(200, 10, txt=f"Field of Study: {field_of_study}", ln=True)

    # Skills
    pdf.ln(2)  # Add spacing before the Skills section
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Skills", ln=True)
    # Line separator after Personal Details
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=skills)

    # Work Experience
    pdf.ln(5)  # Add spacing before the Work Experience section
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Work Experience", ln=True)
    # Line separator after Personal Details
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.set_text_color(0, 0, 0)  # Black

    # Iterate through positions and responsibilities
    # Check responsibilities_list for None or empty list
    if responsibilities_list is None or not responsibilities_list:
        pdf.multi_cell(0, 10, txt="No responsibilities available")
    else:
        for i in range(len(positions_list)):
            pdf.multi_cell(0, 10, txt=f"Position: {positions_list[i]}")
            
            # Check index i is within the valid range of responsibilities_list
            if i < len(responsibilities_list):
                pdf.multi_cell(0, 10, txt=f"Responsibilities: {responsibilities_list[i]}")
            else:
                pdf.multi_cell(0, 10, txt="No responsibilities available for this position")

    # Projects
    pdf.ln(5)  # Add spacing before the Projects section
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Projects", ln=True)
    # Line separator after Personal Details
    pdf.set_draw_color(0, 0, 139)  # Dark Blue
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=projects)

    # Academic and Extracurricular Achievements
    pdf.ln(10)  # Add spacing before the Achievements section
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Achievements", ln=True)
    # Line separator after Personal Details
    pdf.set_draw_color(0, 0, 139)  # Dark Blue
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=achievements)

    return pdf

# Streamlit App
st.title("# Resume Builder")

# Gather personal information
first_name = st.text_input("First name")
last_name = st.text_input("Last name")
phone = st.text_input("Phone")
address = st.text_input("Email Address")

# Qualifications
st.markdown("<h2 style='color: #87CEFA;'>Enter Your Qualification</h2>", unsafe_allow_html=True)
college_name = st.text_input("College name")
degree = st.text_input("Degree")
field_of_study = st.text_input("Field of Study")
skills = st.text_area("List your skills, separated by |.")

# Work Experience, Projects, and Achievements
st.markdown("<h2 style='color: #87CEFA;'>Work Experience</h2>", unsafe_allow_html=True)

# Gather positions and responsibilities
positions = st.text_area("Positions (Enter each position on a new line)")
responsibilities = st.text_area("Responsibilities (Enter each responsibility on a new line)")

st.markdown("<h2 style='color: #87CEFA;'>Projects</h2>", unsafe_allow_html=True)
projects = st.text_area("Projects (Enter each project on a new line)")

st.markdown("<h2 style='color: #87CEFA;'>Academic and Extracurricular Achievements</h2>", unsafe_allow_html=True)
achievements = st.text_area("Academic and Extracurricular Achievements (Enter each achievement on a new line)")

# User description input
user_description = st.text_area("Enter a brief description about yourself (this will appear in the header of the PDF)")

# Create and Download PDF
if st.button("Download Resume"):
    # Convert input strings to lists
    positions_list = [pos.strip() for pos in positions.split('\n')]
    responsibilities_list = [resp.strip() for resp in responsibilities.split('\n')]
    
    pdf = create_resume_pdf(first_name, last_name, phone, address, college_name, degree, field_of_study, skills, positions_list, responsibilities_list, projects, achievements, user_description)
    pdf_output = pdf.output(dest="S").encode("latin1")
    st.download_button(label="Download Resume", data=pdf_output, file_name="resume.pdf", mime="application/pdf")
