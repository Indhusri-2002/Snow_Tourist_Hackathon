import streamlit as st
import pandas as pd
import os
from PIL import Image, ImageOps
from utils.data_loader import load_datasets
import base64
import streamlit.components.v1 as components
from components.Artforms import render_artforms_section
from components.CulturalExperience import render_experiences_section

def render():
    # CSS and JS
    st.markdown("""
        <style>
            .full-width-img img {
                width: 100% !important;
                height: auto;
                display: block;
                margin: 0;
                padding: 0;
            }
            .center-container {
                max-width: 1000px;
                margin: auto;
                padding: 2rem;
            }
        </style>
        <script>
            function scrollToSection(section) {
                const el = document.getElementsByName(section)[0];
                if (el) {
                    el.scrollIntoView({ behavior: "smooth" });
                }
            }
        </script>
    """, unsafe_allow_html=True)

    # Load Data
    dfs = load_datasets()

    df_artforms = dfs["art_forms"]
    df_experiences = dfs["experiences"]
    # Container
    st.markdown('<div class="center-container">', unsafe_allow_html=True)

    # Banner
    st.markdown('<div class="full-width-img">', unsafe_allow_html=True)
    st.image("images/home_page.jpeg", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Intro
    st.markdown("##")
    st.markdown("### Explore the Art, Culture, and Heritage of India")
    st.write("""
        India is a land of diverse traditions, vibrant festivals, and rich history. 
        From the classical dance forms of Bharatnatyam and Kathak to the architectural marvels of ancient temples 
        and forts, every corner of India tells a unique story. Dive into the artistic soul of the country 
        and uncover experiences that go beyond sightseeing—immerse yourself in its living heritage.
    """)

    # Images with Buttons
    art_image = Image.open("images/art.jpeg")
    culture_image = Image.open("images/cultural_experience.jpeg")
    art_image_resized = ImageOps.fit(art_image, (600, 400), Image.Resampling.LANCZOS)
    culture_image_resized = ImageOps.fit(culture_image, (600, 400), Image.Resampling.LANCZOS)

    col1, col2 = st.columns(2)

    with col1:
        st.image(art_image_resized, caption="**Art Forms of India**", use_container_width=True)
        if st.button("View Different Art forms of India", key="art_btn"):
            st.session_state.active_tab = "art"
            st.markdown('<script>scrollToSection("art-section")</script>', unsafe_allow_html=True)

    with col2:
        st.image(culture_image_resized, caption="**Cultural Experiences in India**", use_container_width=True)
        if st.button("Explore the Cultural Experiences of India", key="culture_btn"):
            st.session_state.active_tab = "culture"
            st.markdown('<script>scrollToSection("culture-section")</script>', unsafe_allow_html=True)

    # Divider
    st.markdown("<hr />", unsafe_allow_html=True)

    # Render Sections
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "art"

    if st.session_state.active_tab == "art":
        render_artforms_section(df_artforms)
    else:
        render_experiences_section(df_experiences)

    st.markdown('</div>', unsafe_allow_html=True)
