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
}
PROJECTS = {
    "► [Nifty 50 Analyzer](https://lnkd.in/gdC-6Aem)": "Created a SARIMA-powered forecasting dashboard using Python, DAX, and Yahoo Finance data to predict trends and enhance trading decisions through RSI, SMA, EMA, and MACD indicators.",

    "► AI Interview Coach": "Developed a web-based mock interview platform using Gemini Pro 2.5 for question generation and OpenAI Whisper for real-time speech-to-text analysis, with NLP-based scoring across 5 skill metrics.",

    "► Price Transmission Analysis": "Utilized Python and Power BI to analyze 5 years of wholesale and retail commodity prices, applying ADF tests to evaluate seasonal pricing and transmission trends of onion, tomato, and potato across Indian states.",
    
    "► [Market Basket Analysis](https://www.linkedin.com/posts/sanchit-jain-63599217a_market-basket-analysis-activity-7244404956206653440-a0e8?utm_source=share&utm_medium=member_desktop&rcm=ACoAACqA9gkBkRrKjlNu50wYCT_z7PH51TwLAJc)": "Built a predictive recommendation engine using the Apriori algorithm on custom retail datasets, improving POS-based suggestions with Python, NumPy, and Pandas.",
    
    "► [Customer Churn Rate & Diagnostics](https://drive.google.com/file/d/1ulERYAa0QoGkx1uAiBMYKdxF_4XCBPaX/view?usp=sharing)": "Designed 3 Power BI KPI dashboards on PwC datasets with 5000+ data points to visualize churn risks, customer satisfaction, and diversity metrics for strategic decisions." 
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
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.image(profile_pic, use_container_width =True)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
with col3:
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

st.write('---')
col1, col2= st.columns(2, gap="small")
# --- EXPERIENCE & QUALIFICATIONS ---
with col1:
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - ✔️ Experience in data-driven business analysis and cloud solution development 
        - ✔️ B.Tech in Information Technology & PGDM in Big Data Analytics
        - ✔️ Strong command of Power BI, SQL, Azure Data Factory, & Python 
        - ✔️ Delivered performance optimization, ETL automation, & reports  
        - ✔️ Certificted with Microsoft in [Azure Fundamentals](https://drive.google.com/file/d/1LAbc9GChcDmwYzffNckcTzpvGU8GAJUl/view?usp=sharing) & [Data Fundamentals](https://drive.google.com/file/d/1EQN1WY9eaSCEYKAz8KDponwIP06ZeiDb/view?usp=sharing)
        """
    )
# --- SKILLS ---
with col2:
    st.subheader("Hard Skills")
    st.write(
        """
        - ► Programming: Python, SQL, PL/SQL, R, C# .NET
        - ► Tools: Power BI, Tableau, Power Apps, Power Automate, Excel Macros
        - ► Cloud & ETL: Azure Data Factory, Azure SQL, Oracle Apex
        - ► Analytics: ADF tests, Market Basket Analysis, KPI dashboards
        """
        )

# --- WORK HISTORY ---
st.write("---")
st.markdown(
    """
    <div style="height:2px;background-color:white;padding:0"></div>
    """,
    unsafe_allow_html=True
)
st.subheader("Work History")
st.markdown(
    """
    <div style="height:2px;background-color:white;"></div>
    """,
    unsafe_allow_html=True
)
st.write('\n')
st.write("", "**HR Analyst | Larsen & Toubro Ltd.**")
st.write("April 2025 – June 2025")
st.write(
    """
- ► Analyzed 150+ exit interviews to extract sentiment & clustered 500+ employee data points, revealing 
key turnover insights for strategic planning
- ► Explored global career pathing tools like Phenom, TalentGuard etc. to benchmark KPIs & crafting role-based 
skill matrix for enhanced employee engagement & retention
- ► Developed mock Python Streamlit web app for career pathing & proposed advanced predictive career solutions
"""
)

st.write('\n')
st.write("", "**Cloud Solutions Consultant | Fusion Practices Technologies Pvt. Ltd.**")
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

st.write("", "**Oracle Technical Intern | Fusion Practices Technologies Pvt. Ltd.**")
st.write("Feb 2022 – Jul 2022")
st.write(
    """
- ► Developed Oracle Apex apps with secure REST API interactions
- ► Led cross-functional collaboration for UK insurance client project delivery
- ► Trained users and stakeholders via MS Teams to improve platform adoption
"""
)

st.write("", "**Data Engineering Intern | Celebal Technologies Pvt. Ltd.**")
st.write("Aug 2021 – Jan 2022")
st.write(
    """
- ► Migrated data from 5+ enterprises to Azure SQL with custom automation pipelines
- ► Built 10+ Python scripts to automate tasks, boosting workflow speed and accuracy
- ► Documented key insights and created reports on data transformation workflows
"""
)

# --- Projects & Accomplishments ---
st.write("---")
st.markdown(
    """
    <div style="height:2px;background-color:white;padding:0"></div>
    """,
    unsafe_allow_html=True
)
st.subheader("Projects & Accomplishments")
st.markdown(
    """
    <div style="height:2px;background-color:white;"></div>
    """,
    unsafe_allow_html=True
)
st.write('\n')
for project, details in PROJECTS.items():
    st.write(f"{project}: {details}")
