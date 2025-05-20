import streamlit as st
from streamlit_option_menu import option_menu

from pages import home, analytics, about

st.set_page_config(page_title="My Streamlit App", layout="wide")

# Top Navigation Bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Analytics", "About"],
    icons=["house", "bar-chart-line", "gear"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Page Routing
if selected == "Home":
    home.render()
elif selected == "Analytics":
    analytics.render()
elif selected == "About":
    about.render()
