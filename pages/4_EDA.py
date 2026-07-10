import streamlit as st
import pandas as pd
import plotly.express as px
import gc

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📈",
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
    df = pd.read_csv("Cleaned_Household_Power_Consumption.xls")
    return df


df = load_data()

st.markdown("""
<div class="home-card">
<h1 style="text-align:center;">
📈 Exploratory Data Analysis
</h1>

<p style="text-align:center;font-size:18px;">
Interactive Household Power Consumption Dashboard
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

total_records = len(df)
avg_power = round(df["Global_active_power"].mean(),2)
avg_voltage = round(df["Voltage"].mean(),2)
avg_current = round(df["Global_intensity"].mean(),2)

c1,c2,c3,c4 = st.columns(4)

c1.metric("📄 Records",f"{total_records:,}")
c2.metric("⚡ Avg Power",avg_power)
c3.metric("🔌 Avg Voltage",avg_voltage)
c4.metric("🔋 Avg Current",avg_current)

st.divider()

st.sidebar.header("📊 EDA Filters")

months = sorted(df["Month"].dropna().unique())

selected_months = st.sidebar.multiselect(
    "Select Month",
    months,
    default=months
)

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

selected_column = st.sidebar.selectbox(
    "Select Numeric Column",
    numeric_cols
)

filtered_df = df[df["Month"].isin(selected_months)]

st.success(f"Showing {len(filtered_df):,} Records")

st.divider()
st.subheader("📈 Hourly Average Power Consumption")

hourly = (
    filtered_df
    .groupby("Hour", as_index=False)["Global_active_power"]
    .mean()
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
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("🔌 Voltage Trend")

voltage_df = filtered_df.head(1000)

fig = px.line(
    voltage_df,
    x="Datetime",
    y="Voltage",
    title="Voltage Over Time"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("📊 Active vs Reactive Power")

scatter_df = filtered_df.sample(
    n=min(1000, len(filtered_df)),
    random_state=42
)

fig = px.scatter(
    scatter_df,
    x="Global_active_power",
    y="Global_reactive_power",
    color="Month",
    title="Active vs Reactive Power"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("📉 Distribution Analysis")

fig = px.histogram(
    filtered_df,
    x=selected_column,
    nbins=40,
    title=f"Distribution of {selected_column}"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()
st.subheader("📦 Box Plot")

fig = px.box(
    filtered_df,
    y=selected_column,
    color="Month",
    title=f"Box Plot of {selected_column}"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("🥧 Sub Metering Distribution")

meter_df = pd.DataFrame({
    "Meter": [
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3"
    ],
    "Consumption": [
        filtered_df["Sub_metering_1"].sum(),
        filtered_df["Sub_metering_2"].sum(),
        filtered_df["Sub_metering_3"].sum()
    ]
})

fig = px.pie(
    meter_df,
    names="Meter",
    values="Consumption",
    hole=0.5,
    title="Sub Metering Distribution"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("📅 Monthly Average Consumption")

monthly = (
    filtered_df
    .groupby("Month", as_index=False)["Global_active_power"]
    .mean()
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
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("🔥 Correlation Matrix")

corr = filtered_df[numeric_cols].corr()

fig = px.imshow(
    corr.round(2),
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r"
)

fig.update_layout(
    template="plotly_dark",
    height=550
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("⚡ Peak Consumption Hours")

peak = (
    filtered_df
    .groupby("Hour", as_index=False)["Global_active_power"]
    .mean()
    .sort_values(
        by="Global_active_power",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    peak,
    x="Hour",
    y="Global_active_power",
    color="Global_active_power",
    title="Top 10 Peak Hours"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()
st.subheader("⚡ Outside Consumption Analysis")

outside = (
    filtered_df
    .groupby("Hour", as_index=False)["Outside_Consumption"]
    .mean()
)

fig = px.line(
    outside,
    x="Hour",
    y="Outside_Consumption",
    markers=True,
    title="Average Outside Consumption by Hour"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, width="stretch")

del fig
gc.collect()

st.divider()

st.subheader("📋 Statistical Summary")

summary = filtered_df[numeric_cols].describe().T

st.dataframe(
    summary,
    width="stretch",
    height=450
)

st.divider()

st.subheader("💡 Key Business Insights")

c1, c2 = st.columns(2)

with c1:
    st.success(f"""
### Highest Active Power
**{filtered_df['Global_active_power'].max():.2f} kW**
""")

    st.info(f"""
### Average Voltage
**{filtered_df['Voltage'].mean():.2f} V**
""")

with c2:
    st.warning(f"""
### Maximum Current
**{filtered_df['Global_intensity'].max():.2f} A**
""")

    st.success(f"""
### Average Outside Consumption
**{filtered_df['Outside_Consumption'].mean():.2f}**
""")

st.divider()

st.subheader("📥 Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered CSV",
    data=csv,
    file_name="Filtered_EDA_Data.csv",
    mime="text/csv",
    key="eda_download_csv"
)

st.divider()

st.markdown("""
<div class="footer-box" style="text-align:center;">

<h2>📈 Exploratory Data Analysis Dashboard</h2>

<p>
Household Power Consumption Analysis
</p>

<hr>

<p>
Developed By <b>Pawan Lokhande</b>
</p>

<p>
Python • Pandas • Plotly • Streamlit
</p>

<p>
Version 2.1
</p>

</div>
""", unsafe_allow_html=True)

gc.collect()