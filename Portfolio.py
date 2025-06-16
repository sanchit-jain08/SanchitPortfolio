import streamlit as st
from PIL import Image

# --------- GENERAL SETTINGS ----------
st.set_page_config(page_title="Sanchit Jain Portfolio", layout="wide")
st.title("👨‍💼 Sanchit Jain")
st.subheader("Cloud Solutions Consultant | Data Enthusiast | Power BI Expert")

# --------- CONTACT SECTION ----------
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Sanchit Jain", width=150)  # Replace with your image URL or local file
    st.write("📧 sanchit.jain24b@gim.ac.in")
    st.write("📞 +91-9255543449")
    st.markdown("[LinkedIn](https://linkedin.com)")

# --------- ABOUT ME ----------
st.header("🧾 About Me")
st.write("""
Data-driven Cloud Consultant with experience in Power BI, Azure, and Data Engineering. 
Currently pursuing PGDM in Big Data Analytics at Goa Institute of Management.
""")

# --------- EXPERIENCE ----------
st.header("💼 Professional Experience")

st.subheader("Cloud Solutions Consultant | Fusion Practices Technologies (Aug 2022 – May 2024)")
st.markdown("""
- Led requirements gathering for UK-based insurance client.
- Implemented advanced Power BI reports with DAX.
- Reduced query processing time by 20% using SQL optimization.
- Built 10+ APIs in C# .NET, enhancing data integration.
- Developed ETL pipelines with Azure Data Factory.
""")

st.subheader("Oracle Technical Intern | Fusion Practices (Feb 2022 – Jul 2022)")
st.markdown("""
- Conducted user training sessions and built Oracle APEX applications.
- Collaborated cross-functionally for real-time client projects.
""")

st.subheader("Data Engineering Intern | Celebal Technologies (Aug 2021 – Jan 2022)")
st.markdown("""
- Migrated data from 5+ enterprises to Azure SQL.
- Automated workflows with Python and SQL pipelines.
""")

# --------- EDUCATION ----------
st.header("🎓 Education")
st.write("""
- **PGDM (Big Data Analytics)** – Goa Institute of Management (2024–2026, Pursuing)  
- **B.Tech (Information Technology)** – Manipal University Jaipur (84.10%, 2018–2022)  
- **HSC** – Modern Public School, Bhiwadi (88.80%, 2017–2018)  
- **SSC** – Modern Public School, Bhiwadi (91.20%, 2015–2016)
""")

# --------- PROJECTS ----------
st.header("🧪 Projects")

st.subheader("Price Transmission Analysis")
st.write("""
- Scraped 5 years of market data and visualized it with Power BI.
- Applied econometric tests like ADF to study price dynamics.
""")

st.subheader("Market Basket Analysis")
st.write("""
- Applied apriori algorithm using Python to build recommendation logic.
- Published a technical article on automated suggestions in sales.
""")

st.subheader("Churn Analysis & Customer Diagnostics")
st.write("""
- Created Power BI dashboards to visualize churn, satisfaction, and diversity metrics using PwC data.
""")

# --------- CERTIFICATIONS ----------
st.header("📜 Certifications")
st.write("""
- **Microsoft Azure Fundamentals (AZ-900)**  
- **Azure Data Fundamentals (DP-900)**  
- **KPMG Forage Data Analytics Consulting Virtual Internship**
""")

# --------- SKILLS ----------
st.header("🧠 Core Competencies")
st.write("""
- **Tools**: Power BI, Azure, Tableau, Excel Macros, Power Apps, Power Automate, Oracle APEX  
- **Languages**: SQL, Python, R, PL/SQL, C# .NET
""")

# --------- FOOTER ----------
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
