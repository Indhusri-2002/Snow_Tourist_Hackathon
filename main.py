import streamlit as st
from screens import home, analytics, about

st.set_page_config(page_title="India Tourism Dashboard", layout="wide")

st.markdown("""
    <style>
    /* General tab styling */
    .stTabs [role="tab"] {
        padding: 12px 24px;
        color: #444;
        background-color: #f0f0f0;
        border: none;
        box-shadow: none;
    }

    /* Hover effect */
    .stTabs [role="tab"]:hover {
        background-color: #e0e0e0;
        color: #000;
    }

    /* Selected tab styling */
    .stTabs [aria-selected="true"] {
        background-color: #FF4B4B !important;
        color: white !important;
        font-weight: bold;
        border-bottom: none !important;
        box-shadow: none !important;
    }

    /* Remove the orange bottom border/indicator */
    .stTabs [role="tab"]:focus {
        box-shadow: none !important;
        border: none !important;
        outline: none !important;
    }

    /* Extra: remove the underline line below the tab bar */
    .stTabs {
        border-bottom-: none !important;
    }
    </style>
""", unsafe_allow_html=True)



tab = st.tabs(["Explore India", "Tourism Insights", "Undiscovered India"])

with tab[0]:
    home.render()
with tab[1]:
    analytics.render()
with tab[2]:
    about.render()
