import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home | Power Dashboard",
    page_icon="⚡",
    layout="wide"
)

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Household_Power_Consumption.xls")

df = load_data()

total_records = len(df)
total_columns = len(df.columns)
numeric_columns = len(df.select_dtypes(include="number").columns)
missing_values = int(df.isnull().sum().sum())

st.markdown("""
<div class="home-card">
<h1 style="text-align:center;">
⚡ Household Power Consumption Dashboard
</h1>

<p style="text-align:center;font-size:18px;">
Professional Interactive Data Analytics Dashboard
</p>

<p style="text-align:center;">
Python • Pandas • Plotly • Streamlit
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📄 Total Records", f"{total_records:,}")
c2.metric("📊 Total Columns", total_columns)
c3.metric("📈 Numeric Columns", numeric_columns)
c4.metric("❌ Missing Values", missing_values)

st.divider()
st.subheader("📂 Dashboard Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="home-card">
        <h3>📊 Dataset</h3>
        <p>
        Explore the dataset with search, preview,
        statistics and download functionality.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="home-card">
        <h3>📈 Exploratory Data Analysis</h3>
        <p>
        Analyze trends, correlations,
        distributions and interactive charts.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="home-card">
        <h3>🧹 Data Cleaning</h3>
        <p>
        Check missing values,
        duplicate records,
        data quality and cleaning report.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="home-card">
        <h3>👨‍💻 About Project</h3>
        <p>
        Project overview,
        technologies,
        workflow and developer information.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("💻 Technology Stack")

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("""
    <div class="home-card">
    <h3>🐍 Python</h3>
    <p>Core Programming Language</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="home-card">
    <h3>🐼 Pandas</h3>
    <p>Data Manipulation & Cleaning</p>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="home-card">
    <h3>📊 Plotly</h3>
    <p>Interactive Visualizations</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="home-card">
    <h3>📈 Matplotlib</h3>
    <p>Statistical Charts</p>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="home-card">
    <h3>🎨 Streamlit</h3>
    <p>Interactive Dashboard Framework</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="home-card">
    <h3>📋 Excel Dataset</h3>
    <p>Household Power Consumption</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("🚀 Dashboard Features")

f1, f2, f3 = st.columns(3)

with f1:
    st.info("📂 Dataset Exploration")
    st.info("📈 Interactive Charts")
    st.info("🔎 Search Records")

with f2:
    st.success("📥 Download Dataset")
    st.success("🧹 Data Cleaning")
    st.success("📊 Statistical Analysis")

with f3:
    st.warning("⚡ Power Analysis")
    st.warning("🔥 Correlation Analysis")
    st.warning("📉 Trend Analysis")

st.divider()
st.subheader("📈 Project Workflow")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("""
    <div class="home-card">
    <h4>📥 Collect</h4>
    <p>Load raw household power data.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="home-card">
    <h4>🧹 Clean</h4>
    <p>Handle missing values and duplicates.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="home-card">
    <h4>📊 Analyze</h4>
    <p>Perform EDA and statistical analysis.</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="home-card">
    <h4>📈 Visualize</h4>
    <p>Create interactive charts and dashboards.</p>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="home-card">
    <h4>💡 Insights</h4>
    <p>Generate meaningful business insights.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("⭐ Why This Project?")

st.markdown("""
<div class="home-card">

### 🎯 Objective

This dashboard was developed to analyze household electricity consumption using
interactive visualizations and data analytics techniques.

### ✨ Key Highlights

- Interactive Dashboard
- Professional Dark Theme
- Data Cleaning Module
- Exploratory Data Analysis
- Interactive Plotly Charts
- CSV Download Support
- Business Insights
- Resume & Portfolio Ready

</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("👨‍💻 Developer")

left, right = st.columns([1, 2])

with right:
    st.markdown("""
    <div class="footer-box">

    <h2 style="color:#00E5FF; margin-bottom:5px;">
    👨‍💻 Pawan Lokhande
    </h2>

    <h4 style="color:white;">
    B.Tech CSE (Data Science)
    </h4>

    <hr>

    <h3 style="color:#00E5FF;">
    🛠 Technical Skills
    </h3>

    ✅ Python<br>
    ✅ Pandas<br>
    ✅ NumPy<br>
    ✅ Plotly<br>
    ✅ Streamlit<br>
    ✅ Data Visualization<br>
    ✅ Data Cleaning<br>
    ✅ Exploratory Data Analysis

    <br><br>

    <h3 style="color:#00E5FF;">
    🚀 Project Focus
    </h3>

    • Interactive Dashboard Development<br>
    • Data Analytics & Visualization<br>
    • Business Insights Generation<br>
    • Professional Portfolio Projects

    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("📊 Project Summary")

a, b, c = st.columns(3)

with a:
    st.metric("Dashboard Pages", "5")

with b:
    st.metric("Charts", "10+")

with c:
    st.metric("Project Version", "2.0")

st.divider()

st.markdown("""
<div class="footer-box" style="text-align:center;">

<h2>⚡ Household Power Consumption Dashboard</h2>

<p>
Professional Data Analytics Portfolio Project
</p>

<hr>

<p>
Developed by <b>Pawan Lokhande</b>
</p>

<p>
Python • Pandas • Plotly • Streamlit
</p>

<p>
Version 2.0 | © 2026
</p>

</div>
""", unsafe_allow_html=True)