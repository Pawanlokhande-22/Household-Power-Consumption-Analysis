import streamlit as st


st.set_page_config(
    page_title="Power Consumption Dashboard",
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

with st.sidebar:

    st.markdown(
        """
        <div style="
        background:#1e293b;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:1px solid #334155;
        ">

        <h1 style="
        color:white;
        font-size:40px;
        ">
        ⚡
        </h1>

        <h2 style="
        color:white;
        ">
        Power Analytics
        </h2>

        <p style="
        color:#cbd5e1;
        ">
        Household Energy
        <br>
        Consumption Dashboard
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    st.markdown(
        """
        <div style="
        background:#020617;
        padding:15px;
        border-radius:12px;
        ">

        <p style="
        color:white;
        font-size:16px;
        ">
        Dashboard Modules
        </p>

        <p style="
        color:#cbd5e1;
        line-height:2;
        ">
        🏠 Home
        <br>
        📊 Dataset Analysis
        <br>
        📈 EDA Visualization
        <br>
        🧹 Data Cleaning
        <br>
        👨‍💻 About Project
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    st.markdown(
        """
        <div style="
        background:#1e293b;
        padding:15px;
        border-radius:12px;
        text-align:center;
        ">

        <p style="
        color:#cbd5e1;
        ">
        Developed By
        </p>

        <h3 style="
        color:white;
        ">
        Pawan Lokhande
        </h3>

        <p style="
        color:#cbd5e1;
        ">
        B.Tech CSE Data Science
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )



st.markdown(
    """
    <div style="
    background:linear-gradient(135deg,#1e293b,#020617);
    padding:45px;
    border-radius:25px;
    text-align:center;
    border:1px solid #334155;
    ">

    <h1 style="
    color:white;
    font-size:45px;
    ">
    ⚡ Household Power Consumption Dashboard
    </h1>


    <p style="
    color:#cbd5e1;
    font-size:20px;
    ">
    Interactive Data Analytics Platform for
    Electricity Consumption Analysis
    </p>


    <p style="
    color:#94a3b8;
    ">
    Python | Pandas | Matplotlib | Seaborn | Streamlit
    </p>


    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown(
        """
        <div class="home-card">

        <h3>
        Data Analysis
        </h3>

        <p>
        Explore and analyze household
        power consumption records.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        """
        <div class="home-card">

        <h3>
        Visualization
        </h3>

        <p>
        Generate charts and discover
        hidden consumption patterns.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        """
        <div class="home-card">

        <h3>
        Insights
        </h3>

        <p>
        Convert raw data into
        meaningful business insights.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


st.markdown(
    """
    <div class="footer-box">

    <h3>
    Household Power Consumption Dashboard
    </h3>

    <p>
    Professional Data Analytics Project
    <br>
    Developed By Pawan Lokhande
    </p>

    </div>
    """,
    unsafe_allow_html=True
)