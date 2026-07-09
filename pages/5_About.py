import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
    layout="wide"
)

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.markdown("""
<div class="home-card">
<h1 style="text-align:center;">
👨‍💻 About the Project
</h1>

<p style="text-align:center;font-size:18px;">
Professional Household Power Consumption Dashboard
</p>

<p style="text-align:center;">
Version 2.0
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1,2])

with right:

    st.markdown("""
<div class="footer-box">

<h2 style="color:#00E5FF;">
Pawan Lokhande
</h2>

<h4 style="color:white;">
B.Tech CSE (Data Science)
</h4>

<hr>

<h3 style="color:#00E5FF;">
🎯 Career Profile
</h3>

• Python Developer<br>
• Data Analyst<br>
• Dashboard Developer<br>
• Data Visualization Enthusiast

</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🎓 Education")

st.markdown("""
<div class="home-card">

### Bachelor of Technology (B.Tech)

**Branch:** Computer Science & Engineering (Data Science)

Currently focused on developing practical skills in:

- Python Programming
- Data Analytics
- Data Visualization
- Dashboard Development
- Exploratory Data Analysis

</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("💻 Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="home-card">

### Programming

✅ Python

✅ NumPy

✅ Basic SQL

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="home-card">

### Data Analytics

✅ Pandas

✅ Data Cleaning

✅ EDA

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="home-card">

### Visualization

✅ Plotly

✅ Matplotlib

✅ Streamlit

</div>
""", unsafe_allow_html=True)
    
    st.divider()

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown("""
    <div class="home-card">

    <h3>Programming</h3>

    🐍 Python<br>
    🔢 NumPy<br>
    📊 Pandas

    </div>
    """, unsafe_allow_html=True)

with tech2:
    st.markdown("""
    <div class="home-card">

    <h3>Visualization</h3>

    📈 Plotly<br>
    📉 Matplotlib<br>
    🎨 Streamlit

    </div>
    """, unsafe_allow_html=True)

with tech3:
    st.markdown("""
    <div class="home-card">

    <h3>Dataset</h3>

    📄 Excel Dataset<br>
    📋 Data Cleaning<br>
    📊 Exploratory Data Analysis

    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("🚀 Dashboard Features")

feature1, feature2 = st.columns(2)

with feature1:
    st.success("📂 Dataset Overview")
    st.success("📈 Interactive EDA")
    st.success("🧹 Data Cleaning")
    st.success("📊 Statistical Analysis")
    st.success("📥 CSV Download")

with feature2:
    st.info("🔍 Search & Filter")
    st.info("📉 Interactive Charts")
    st.info("📋 Data Quality Report")
    st.info("💡 Business Insights")
    st.info("🌙 Professional Dark Theme")

st.divider()

st.subheader("📊 Project Workflow")

st.markdown("""
<div class="home-card">

📥 Dataset Collection

⬇

🧹 Data Cleaning

⬇

📈 Exploratory Data Analysis

⬇

📊 Interactive Visualization

⬇

💡 Business Insights

</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🎯 Career Objective")

st.markdown("""
<div class="footer-box">

I am a Computer Science (Data Science) student with a strong interest in
Python, Data Analytics and Dashboard Development.

This project demonstrates my practical skills in data cleaning,
exploratory data analysis, interactive dashboard development,
and business insight generation using modern Python libraries.

My goal is to build real-world analytics projects that solve
practical business problems while continuously improving my
technical and analytical skills.

</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("📈 Project Statistics")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric("Dashboard Pages", "5")

with s2:
    st.metric("Charts", "10+")

with s3:
    st.metric("Technologies", "6")

with s4:
    st.metric("Version", "2.0")

    st.divider()

st.subheader("🚀 Future Scope")

future1, future2 = st.columns(2)

with future1:
    st.markdown("""
<div class="home-card">

### Future Improvements

✅ Machine Learning Integration

✅ Power Consumption Prediction

✅ Real-Time Dashboard

✅ Database Connectivity

✅ Cloud Deployment

</div>
""", unsafe_allow_html=True)

with future2:
    st.markdown("""
<div class="home-card">

### Planned Enhancements

✅ User Authentication

✅ Report Generation (PDF)

✅ Export to Excel

✅ Advanced Business Analytics

✅ Mobile Friendly Dashboard

</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🏆 Project Achievements")

a1, a2, a3 = st.columns(3)

with a1:
    st.success("✅ Interactive Dashboard")

with a2:
    st.success("✅ Data Cleaning")

with a3:
    st.success("✅ Professional UI")

a4, a5, a6 = st.columns(3)

with a4:
    st.success("✅ Exploratory Data Analysis")

with a5:
    st.success("✅ Business Insights")

with a6:
    st.success("✅ Portfolio Ready")

st.divider()

st.subheader("📞 Contact")

st.markdown("""
<div class="footer-box">

### 👨‍💻 Developer

**Pawan Lokhande**

🎓 B.Tech CSE (Data Science)

📍 Burhanpur, Madhya Pradesh

💻 Skills

• Python

• Pandas

• NumPy

• Plotly

• Streamlit

• Data Visualization

• Data Cleaning

• Exploratory Data Analysis

</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="footer-box" style="text-align:center;">

<h2>⚡ Household Power Consumption Dashboard</h2>

<h4>Professional Data Analytics Portfolio Project</h4>

<hr>

<h3>Developed by Pawan Lokhande</h3>

<p>
Python • Pandas • NumPy • Plotly • Streamlit
</p>

<p>
Version 2.0 | © 2026
</p>

</div>
""", unsafe_allow_html=True)

st.balloons()