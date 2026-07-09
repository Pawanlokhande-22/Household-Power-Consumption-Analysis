import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Household_Power_Consumption.xls")

df = load_data()

total_records = len(df)
total_columns = len(df.columns)
numeric_columns = len(df.select_dtypes(include="number").columns)
missing_values = int(df.isnull().sum().sum())
duplicate_rows = int(df.duplicated().sum())

st.markdown("""
<div class="home-card">
<h1 style="text-align:center;">📂 Dataset Dashboard</h1>
<p style="text-align:center;font-size:18px;">
Household Power Consumption Dataset Overview
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("📄 Records", f"{total_records:,}")
c2.metric("📊 Columns", total_columns)
c3.metric("🔢 Numeric", numeric_columns)
c4.metric("❌ Missing", missing_values)
c5.metric("📋 Duplicates", duplicate_rows)

st.divider()

st.subheader("📑 Dataset Preview")

tab1, tab2, tab3 = st.tabs(
    ["First 10 Rows", "Last 10 Rows", "Random Sample"]
)

with tab1:
    st.dataframe(df.head(10), use_container_width=True)

with tab2:
    st.dataframe(df.tail(10), use_container_width=True)

with tab3:
    st.dataframe(df.sample(10, random_state=42), use_container_width=True)

st.divider()
st.subheader("🔍 Search & Filter Dataset")

left, right = st.columns([2, 1])

with left:

    search_column = st.selectbox(
        "Select Column",
        df.columns,
        key="dataset_search_column"
    )

    search_value = st.text_input(
        "Search Value",
        key="dataset_search_value"
    )

with right:

    month_options = sorted(df["Month"].dropna().unique().tolist())

    selected_months = st.multiselect(
        "Filter by Month",
        month_options,
        default=month_options,
        key="dataset_month_filter"
    )

filtered_df = df[df["Month"].isin(selected_months)]

if search_value:

    filtered_df = filtered_df[
        filtered_df[search_column]
        .astype(str)
        .str.contains(search_value, case=False, na=False)
    ]

st.success(f"Showing {len(filtered_df):,} Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=450
)

st.divider()

st.subheader("📋 Dataset Information")

info_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Unique Values": df.nunique().values
})

st.dataframe(
    info_df,
    use_container_width=True,
    height=500
)

st.divider()

st.subheader("📊 Dataset Health Report")

h1, h2, h3 = st.columns(3)

completeness = round(
    (
        (df.notnull().sum().sum())
        /
        (df.shape[0] * df.shape[1])
    ) * 100,
    2
)

with h1:
    st.metric(
        "✅ Data Completeness",
        f"{completeness}%"
    )

with h2:
    st.metric(
        "❌ Missing Values",
        missing_values
    )

with h3:
    st.metric(
        "📋 Duplicate Rows",
        duplicate_rows
    )

st.divider()

st.subheader("📈 Missing Values by Column")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing": df.isnull().sum().values
})

st.bar_chart(
    missing_df.set_index("Column")
)
st.divider()

st.subheader("📊 Column Statistics")

numeric_columns = filtered_df.select_dtypes(include="number").columns.tolist()

selected_column = st.selectbox(
    "Select Numeric Column",
    numeric_columns,
    key="dataset_statistics_column"
)

col = filtered_df[selected_column]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Mean", f"{col.mean():.2f}")
c2.metric("Median", f"{col.median():.2f}")
c3.metric("Minimum", f"{col.min():.2f}")
c4.metric("Maximum", f"{col.max():.2f}")

c5, c6, c7, c8 = st.columns(4)

mode_value = col.mode()
mode_display = f"{mode_value.iloc[0]:.2f}" if not mode_value.empty else "N/A"

c5.metric("Mode", mode_display)
c6.metric("Std Dev", f"{col.std():.2f}")
c7.metric("Variance", f"{col.var():.2f}")
c8.metric("Skewness", f"{col.skew():.2f}")

st.divider()

st.subheader("📋 Dataset Memory Information")

memory_usage = (
    df.memory_usage(deep=True).sum() / (1024 * 1024)
)

st.info(f"Dataset Memory Usage : {memory_usage:.2f} MB")

st.divider()

st.subheader("📥 Download Dataset")

download_col1, download_col2 = st.columns(2)

with download_col1:

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download CSV",
        data=csv,
        file_name="Filtered_Dataset.csv",
        mime="text/csv"
    )



    with open("Filtered_Dataset.csv", "rb") as f:
        st.download_button(
            "⬇ Download Csv",
            data=f,
            file_name="Filtered_Dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

st.divider()

st.subheader("⭐ Dataset Quality Score")

score = 100

score -= duplicate_rows * 0.01
score -= missing_values * 0.02

score = max(0, min(100, round(score, 2)))

st.progress(score / 100)

if score >= 95:
    st.success(f"Excellent Dataset Quality : {score}%")
elif score >= 80:
    st.info(f"Good Dataset Quality : {score}%")
elif score >= 60:
    st.warning(f"Average Dataset Quality : {score}%")
else:
    st.error(f"Poor Dataset Quality : {score}%")

st.divider()

st.markdown(
    """
<div class="footer-box" style="text-align:center;">

<h2>📂 Dataset Dashboard</h2>

<p>
Household Power Consumption Analysis
</p>

<hr>

<p>
Developed By <b>Pawan Lokhande</b>
</p>

<p>
Python • Pandas • NumPy • Streamlit
</p>

<p>
Version 2.0
</p>

</div>
""",
    unsafe_allow_html=True
)