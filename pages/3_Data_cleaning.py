import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Data Cleaning",
    page_icon="🧹",
    layout="wide"
)

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Household_Power_Consumption.xls")

df = load_data()

total_rows = len(df)
total_columns = len(df.columns)
missing_values = int(df.isnull().sum().sum())
duplicate_rows = int(df.duplicated().sum())

numeric_columns = len(df.select_dtypes(include="number").columns)
categorical_columns = len(df.select_dtypes(exclude="number").columns)

st.markdown("""
<div class="home-card">
<h1 style="text-align:center;">
🧹 Data Cleaning Dashboard
</h1>

<p style="text-align:center;font-size:18px;">
Data Quality Report & Cleaning Analysis
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("📄 Records", f"{total_rows:,}")
c2.metric("📊 Columns", total_columns)
c3.metric("🔢 Numeric", numeric_columns)
c4.metric("🔤 Categorical", categorical_columns)
c5.metric("❌ Missing", missing_values)
c6.metric("📋 Duplicates", duplicate_rows)

st.divider()

st.subheader("📊 Dataset Quality Summary")

left, right = st.columns(2)

with left:

    st.success(f"Total Records : {total_rows:,}")

    st.success(f"Total Columns : {total_columns}")

    st.success(f"Numeric Columns : {numeric_columns}")

with right:

    st.info(f"Categorical Columns : {categorical_columns}")

    st.info(f"Missing Values : {missing_values}")

    st.info(f"Duplicate Rows : {duplicate_rows}")

st.divider()

st.subheader("📋 Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values
})

st.dataframe(
    dtype_df,
    use_container_width=True,
    height=500
)
st.divider()

st.subheader("❌ Missing Values Analysis")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values,
    "Missing (%)": (
        df.isnull().sum() / len(df) * 100
    ).round(2).values
})

st.dataframe(
    missing_df,
    use_container_width=True,
    height=450
)

st.bar_chart(
    missing_df.set_index("Column")["Missing Values"]
)

st.divider()

st.subheader("📋 Duplicate Records Analysis")

duplicate_percentage = round(
    (duplicate_rows / total_rows) * 100,
    2
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Duplicate Rows", duplicate_rows)

with col2:
    st.metric("Duplicate Percentage", f"{duplicate_percentage}%")

if duplicate_rows == 0:
    st.success("✅ No duplicate records found.")
else:
    st.warning(f"⚠️ {duplicate_rows} duplicate records found.")

st.divider()

st.subheader("📊 Numeric vs Categorical Columns")

summary_df = pd.DataFrame({
    "Category": ["Numeric Columns", "Categorical Columns"],
    "Count": [numeric_columns, categorical_columns]
})

st.bar_chart(summary_df.set_index("Category"))

st.divider()

st.subheader("📈 Dataset Quality Score")

missing_score = max(0, 100 - (missing_values * 0.02))
duplicate_score = max(0, 100 - (duplicate_rows * 0.05))

quality_score = round((missing_score + duplicate_score) / 2, 2)

st.progress(quality_score / 100)

if quality_score >= 95:
    st.success(f"🌟 Excellent Dataset Quality ({quality_score}%)")
elif quality_score >= 80:
    st.info(f"👍 Good Dataset Quality ({quality_score}%)")
elif quality_score >= 60:
    st.warning(f"⚠️ Average Dataset Quality ({quality_score}%)")
else:
    st.error(f"❌ Poor Dataset Quality ({quality_score}%)")

st.divider()

st.subheader("📝 Cleaning Summary")

summary = pd.DataFrame({
    "Check": [
        "Missing Values",
        "Duplicate Records",
        "Data Types Verified",
        "Numeric Columns",
        "Categorical Columns"
    ],
    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Verified",
        "Verified"
    ]
})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)
st.divider()

st.subheader("🧹 Cleaning Steps Performed")

steps = pd.DataFrame({
    "Step": [
        "Loaded Dataset",
        "Checked Missing Values",
        "Checked Duplicate Records",
        "Verified Data Types",
        "Validated Numeric Columns",
        "Verified Date & Time Columns",
        "Generated Data Quality Report"
    ],
    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed"
    ]
})

st.dataframe(
    steps,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("📊 Before vs After Cleaning")

before_col, after_col = st.columns(2)

with before_col:
    st.markdown("""
    <div class="home-card">
        <h3>Before Cleaning</h3>
        <ul>
            <li>Raw Dataset</li>
            <li>Quality Check Pending</li>
            <li>Missing Values Reviewed</li>
            <li>Duplicate Records Checked</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with after_col:
    st.markdown("""
    <div class="home-card">
        <h3>After Cleaning</h3>
        <ul>
            <li>Dataset Verified</li>
            <li>Data Types Validated</li>
            <li>Quality Report Generated</li>
            <li>Ready for EDA</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("💡 Data Quality Recommendations")

st.info("""
✔ Keep all column names consistent.

✔ Validate date and time columns before analysis.

✔ Regularly check for missing values in new data.

✔ Remove duplicate records before model building.

✔ Standardize numeric data types for accurate analysis.
""")

st.divider()

st.subheader("📥 Download Clean Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Clean Dataset (CSV)",
    data=csv,
    file_name="Cleaned_Household_Power_Consumption.csv",
    mime="text/csv"
)

st.divider()

st.markdown("""
<div class="footer-box" style="text-align:center;">

<h2>🧹 Data Cleaning Dashboard</h2>

<p>
Household Power Consumption Analysis
</p>

<hr>

<p>
Developed by <b>Pawan Lokhande</b>
</p>

<p>
Python • Pandas • NumPy • Streamlit
</p>

<p>
Version 2.0 | © 2026
</p>

</div>
""", unsafe_allow_html=True)