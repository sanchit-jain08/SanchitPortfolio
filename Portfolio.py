from pathlib import Path
import streamlit as st
from PIL import Image
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.PNG"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sanchit Jain"
PAGE_ICON = ":bar_chart:"
NAME = "Sanchit Jain"
DESCRIPTION = """
Aspiring Data Analyst with hands-on experience in Power BI, SQL, and Azure, backed by a PGDM in Big Data Analytics. Proven track record in using data insights to drive business decisions, optimize workflows, and support strategic growth. Eager to contribute analytical skills to business development initiatives."""
EMAIL = "sanchit.jain24b@gim.ac.in"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sanchit-jain-63599217a/",
    "GitHub": "https://github.com/sanchit-jain08/",
}
PROJECTS = {
    "🏆 Price Transmission Analysis – Utilized Python and Power BI to analyze 5 years of commodity market data, applying ADF tests to uncover seasonal pricing and transmission patterns across Indian states.",
    "🏆 Market Basket Analysis – Built a Python-based solution using the Apriori algorithm for real-world POS suggestions, boosting recommendation accuracy through custom datasets and advanced analytics.",
    "🏆 Churn Analysis & Customer Diagnostics – Created Power BI dashboards with 5000+ data points to visualize key trends, reduce churn, and guide targeted business strategies using PwC & Forage datasets."
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
with col3:
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
        st.write('\n')


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Experience in data-driven business analysis and cloud solution development
- ✔️ Strong command of Power BI, SQL, Azure Data Factory, and Python scripting
- ✔️ Delivered performance optimization, ETL automation, and reporting for enterprise clients
- ✔️ Skilled in building dashboards, streamlining data workflows, and cross-functional teamwork
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👨‍💻 Programming: Python, SQL, PL/SQL, R, C# .NET
- 📊 Tools: Power BI, Tableau, Power Apps, Power Automate, Excel Macros
- ☁️ Cloud & ETL: Azure Data Factory, Azure SQL, Oracle Apex
- 🛠️ Analytics: ADF tests, Market Basket Analysis, KPI dashboards
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

st.write("🚧", "**Cloud Solutions Consultant | Fusion Practices Technologies Pvt. Ltd.**")
st.write("Aug 2022 – May 2024")
st.write(
    """
- ► Developed Power BI reports and DAX functions across 5 enterprise apps to streamline analysis
- ► Improved SQL database performance, reducing query and data retrieval times by 20% and 15%
- ► Built and deployed 10+ APIs using C# .NET to enhance cross-platform data integration
- ► Automated ETL processes with Azure Data Factory, cutting manual workload by 50%
- ► Created cloud-native Power Apps solutions improving workflow efficiency by 20%
"""
)

st.write("🚧", "**Oracle Technical Intern | Fusion Practices Technologies Pvt. Ltd.**")
st.write("Feb 2022 – Jul 2022")
st.write(
    """
- ► Developed Oracle Apex apps with secure REST API interactions
- ► Led cross-functional collaboration for UK insurance client project delivery
- ► Trained users and stakeholders via MS Teams to improve platform adoption
"""
)

st.write("🚧", "**Data Engineering Intern | Celebal Technologies Pvt. Ltd.**")
st.write("Aug 2021 – Jan 2022")
st.write(
    """
- ► Migrated data from 5+ enterprises to Azure SQL with custom automation pipelines
- ► Built 10+ Python scripts to automate tasks, boosting workflow speed and accuracy
- ► Documented key insights and created reports on data transformation workflows
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")
