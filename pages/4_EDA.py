import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📈",
    layout="wide"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Household_Power_Consumption.xls")

df = load_data()

st.markdown("""
<div class="home-card">
<h1 style="text-align:center;">📈 Exploratory Data Analysis</h1>
<p style="text-align:center;">
Interactive Dashboard for Household Power Consumption
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

avg_power = round(df["Global_active_power"].mean(), 2)
avg_voltage = round(df["Voltage"].mean(), 2)
avg_current = round(df["Global_intensity"].mean(), 2)
missing = int(df.isnull().sum().sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Records", f"{len(df):,}")
c2.metric("Avg Active Power", avg_power)
c3.metric("Avg Voltage", avg_voltage)
c4.metric("Avg Current", avg_current)

st.divider()

st.sidebar.header("EDA Filters")

numeric_cols = [
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3",
    "Total_Submetering",
    "Outside_Consumption"
]

selected_col = st.sidebar.selectbox(
    "Select Numeric Column",
    numeric_cols
)

month_filter = st.sidebar.multiselect(
    "Select Month",
    sorted(df["Month"].unique()),
    default=sorted(df["Month"].unique())
)

filtered_df = df[df["Month"].isin(month_filter)]

st.success(f"Filtered Records : {len(filtered_df):,}")
st.divider()

st.subheader("📈 Hourly Power Consumption Trend")

hourly = (
    filtered_df
    .groupby("Hour")["Global_active_power"]
    .mean()
    .reset_index()
)

fig = px.line(
    hourly,
    x="Hour",
    y="Global_active_power",
    markers=True,
    title="Average Active Power by Hour"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()

st.subheader("⚡ Voltage Trend")

fig = px.line(
    filtered_df.head(3000),
    x="Datetime",
    y="Voltage",
    title="Voltage Over Time"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()

st.subheader("📊 Active vs Reactive Power")

fig = px.scatter(
    filtered_df.sample(
        min(5000, len(filtered_df)),
        random_state=42
    ),
    x="Global_active_power",
    y="Global_reactive_power",
    color="Month",
    title="Active Power vs Reactive Power"
)

fig.update_layout(
    template="plotly_dark",
    height=550
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()

st.subheader("📦 Power Distribution")

fig = px.histogram(
    filtered_df,
    x=selected_col,
    nbins=60,
    title=f"Distribution of {selected_col}"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()

st.subheader("📉 Box Plot")

fig = px.box(
    filtered_df,
    y=selected_col,
    color="Month",
    title=f"Box Plot of {selected_col}"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()

st.subheader("🥧 Sub Metering Distribution")

meter = filtered_df[
    [
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3"
    ]
].sum()

pie = pd.DataFrame(
    {
        "Meter": meter.index,
        "Consumption": meter.values
    }
)

fig = px.pie(
    pie,
    values="Consumption",
    names="Meter",
    hole=0.5,
    title="Sub Metering Consumption"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()

st.subheader("📊 Monthly Average Consumption")

monthly = (
    filtered_df
    .groupby("Month")["Global_active_power"]
    .mean()
    .reset_index()
)

fig = px.bar(
    monthly,
    x="Month",
    y="Global_active_power",
    color="Global_active_power",
    title="Monthly Average Active Power"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

st.subheader("🔥 Correlation Heatmap")

corr = filtered_df[
    [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3",
        "Total_Submetering",
        "Outside_Consumption"
    ]
].corr()

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    aspect="auto",
    title="Correlation Matrix"
)

fig.update_layout(
    template="plotly_dark",
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📋 Statistical Summary")

summary = filtered_df[
    [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3",
        "Total_Submetering",
        "Outside_Consumption"
    ]
].describe().T

st.dataframe(
    summary,
    use_container_width=True
)

st.divider()

st.subheader("📊 Peak Consumption Hours")

peak = (
    filtered_df.groupby("Hour")["Global_active_power"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    peak,
    x="Hour",
    y="Global_active_power",
    color="Global_active_power",
    title="Top 10 Peak Power Consumption Hours"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("⚡ Outside Consumption Analysis")

fig = px.line(
    filtered_df.groupby("Hour")["Outside_Consumption"]
    .mean()
    .reset_index(),
    x="Hour",
    y="Outside_Consumption",
    markers=True,
    title="Average Outside Consumption by Hour"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("💡 Key Business Insights")

col1, col2 = st.columns(2)

with col1:
    st.success(
        f"""
Highest Active Power

{filtered_df['Global_active_power'].max():.2f} kW
"""
    )

    st.info(
        f"""
Average Voltage

{filtered_df['Voltage'].mean():.2f} V
"""
    )

with col2:
    st.warning(
        f"""
Maximum Current

{filtered_df['Global_intensity'].max():.2f} A
"""
    )

    st.success(
        f"""
Average Outside Consumption

{filtered_df['Outside_Consumption'].mean():.2f}
"""
    )

st.divider()

st.subheader("📥 Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered CSV",
    data=csv,
    file_name="Filtered_EDA_Data.csv",
    mime="text/csv"
)

st.divider()

st.markdown(
    """
    <div class="footer-box">

    <h3>📈 Exploratory Data Analysis Completed</h3>

    <p>
    Household Power Consumption Dashboard<br><br>
    Developed By <b>Pawan Lokhande</b><br>
    B.Tech CSE Data Science<br><br>

    Technologies Used<br>
    Python • Pandas • Plotly • Streamlit
    </p>

    </div>
    """,
    unsafe_allow_html=True
)