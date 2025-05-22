import streamlit as st
from screens import home, analytics, about

st.set_page_config(page_title="India Tourism Dashboard", layout="wide")

tab = st.tabs(["Home", "Analytics", "About"])

with tab[0]:
    home.render()
with tab[1]:
    analytics.render()
with tab[2]:
    about.render()
