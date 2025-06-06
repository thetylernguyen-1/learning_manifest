import streamlit as st
import pandas as pd
import sys, os
import matplotlib.pyplot as plt
#import all the figures
from visualization.learning_pyramid import create_capability_pyramid
from visualization.whole_brain_analysis import create_quadrant_pie_chart
from visualization.funnel_improvement import create_leadership_funnel_chart
from visualization.saboteur import create_saboteur_bar_chart
from visualization.radar import create_radar_chart
from visualization.venn_diagram import create_who_how_venn
st.set_page_config(layout="wide")


# CSS
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 2px solid black;
        background-color: white;
        color: black;
        padding: 10px 24px;
        cursor: pointer;
        float: left;
    }
    .stButton > button:hover {
    color: #1588ed;
    border: 2px solid #1588ed;
    }
    .stButton > button:active {
    background-color: white;
    color: #1588ed;
    border: 2px solid #1588ed; 
    }
    .stExpander > div > div > div > button:hover {
        color: #1588ed;
        border: #1588ed;
    }
    .stColumns > div {
        flex: 1;
    }
    .stColumns > div:first-child {
        flex: 0.4;  /* Make the first column smaller */
    }
    .stColumns > div:nth-child(2) {
        flex: 2;  /* Make the second column wider */
    }
    .stColumns > div:last-child {
        flex: 2;  /* Make the third column wider */
    }
    .block-container {
        padding-top: 5rem;
    }
    h3 {
        margin-bottom: 0px;
    }
    .element-container {
        padding-top: 0px;
        margin-top: 0px;
    }
    .metric-box {
    padding: 20px;
    background-color: #f0f2f6;
    border-radius: 10px;
    text-align: center;
    position: relative;
    display: inline-block;
    margin: 10px;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 120px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position above the text */
        left: 50%;
        margin-left: -60px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    .custom-delta {
        color: black; /* Change to any color you want */
        font-size: 18px !important; 
        margin-top: -20px !important; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# CSS 
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #CAE6F1;
    }
    .sidebar-title {
        text-align: center;
        color: #4A4A4A;
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style='text-align: center; color: #2C3E50;'>🌱 Welcome to My Learning Manifest</h1>
    <p style='text-align: center; font-size: 18px; color: #4A4A4A;'>
        A personal journey of growth, reflection, and intentional development.
    </p>
    """, 
    unsafe_allow_html=True
)
# Sidebar 
st.sidebar.markdown(
    "<div class='sidebar-title'>💡 Learning Manifest</div>",
    unsafe_allow_html=True
)
st.sidebar.info("Use the dropdown below to explore different aspects of my learning journey 👇")

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Scroll through to explore more insights.")


page = st.sidebar.selectbox(
    " 🔎 Choose a page:",
    ["Expertise Pyramid", "Embracing the Fear", "Systematic and Long-term Action", "Bridging the Gaps"]
)

if page == "Expertise Pyramid":
    st.title("📋 Aspects of Leadership")

    col1, = st.columns(1)
    with col1:
        st.subheader("Expertise Pyramid")
        fig_pyramid = create_capability_pyramid()
        st.plotly_chart(fig_pyramid, use_container_width=True)
        
        st.subheader("Leadership Capabilities to Improve (by Priority)")
        fig_funnel = create_leadership_funnel_chart()
        st.plotly_chart(fig_funnel, use_container_width= True)

if page == "Embracing the Fear":
    st.title("🙌 Who is learning?")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Saboteur: The Shadow Behind My Decisions")
        fig_saboteur = create_saboteur_bar_chart()
        st.plotly_chart(fig_saboteur, use_container_width= True)

    with col2:
        st.subheader("The Whole-Brain Model Analysis")
        fig_brain = create_quadrant_pie_chart()
        st.plotly_chart(fig_brain, use_container_width=True)

if page == "Systematic and Long-term Action":
    st.title("⭐ From Intention to Impact: Where I Grow Next")

    col1, col2 = st.columns(2)
    categories = ['Social', 'Institutional', 'Physical', 'Digital']

    with col1:
        st.subheader("Vision:")
        current = [5, 6, 5, 3]
        desired = [8, 8, 8, 7]

        fig = create_radar_chart(categories, current, desired, title="Vision Radar")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Accountability:")
        current_acc = [3, 7, 7, 3]
        desired_acc = [5, 8, 8, 5]

        fig = create_radar_chart(categories, current_acc, desired_acc, title="Accountability Radar")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Integrity:")
        current = [4, 6, 6, 5]
        desired = [6, 8, 8, 7]

        fig = create_radar_chart(categories, current, desired, title="Vision Radar")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Influence:")
        current_inf = [3, 5, 5, 3]
        desired_inf = [5, 9, 8, 8]

        fig = create_radar_chart(categories, current_inf, desired_inf, title="Accountability Radar")
        st.plotly_chart(fig, use_container_width=True)

if page == "Bridging the Gaps":
    st.title("Turning Tensions into Synergy")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Optimal time of the day for learning:")
        data = {
            "Work": ["Analytic tasks", "Insight tasks", "Making an impression","Making a decision"],
            "Third Bird":["Early to midmorning", "Late afternoon/early evening","Morning", "Early to midmorning"],
        }
        df = pd.DataFrame(data)
        st.dataframe(df.style.set_properties(**{
    'background-color': "#CAE6F1",
    'color': 'black',
    'border-color': 'gray',
    'text-align': 'center'
}))
    with col2: 
        st.subheader("Turning Tensions into Synergy:")
        fig_venn = create_who_how_venn()
        st.pyplot(fig_venn)






        


