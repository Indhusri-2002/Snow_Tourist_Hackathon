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
                margin : 0;
                padding:0;
                max-width: 1000px;
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
    st.markdown("## Explore the Art, Culture, and Heritage of India")


    # Banner
    st.markdown('<div class="full-width-img">', unsafe_allow_html=True)
    st.image("images/home_page.jpeg", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Intro
    st.markdown("""
    <div style = "margin-bottom : 20px" >
        <h1 style="font-size: 1.5rem;">Discover the Soul of India — One Culture at a Time.</h1>
        <p style="font-size: 1rem;">
            India is a land of diverse traditions, vibrant festivals, and rich history. 
            From the classical dance forms of Bharatnatyam and Kathak to the architectural marvels of ancient temples 
            and forts, every corner of India tells a unique story. Dive into the artistic soul of the country 
            and uncover experiences that go beyond sightseeing—immerse yourself in its living heritage.
            Uncover ancient art forms, hidden cultural gems, and stories that breathe life into every corner of the country.
            This platform brings data-driven insights into India’s vibrant heritage and the impact of responsible tourism.
            Join us in preserving traditions while exploring them—smartly, sustainably, and soulfully.
        </p>
    </div>
""", unsafe_allow_html=True)


    # Images with Buttons
    art_image = Image.open("images/art.jpeg")
    culture_image = Image.open("images/cultural_experience.jpeg")
    art_image_resized = ImageOps.fit(art_image, (600, 400), Image.Resampling.LANCZOS)
    culture_image_resized = ImageOps.fit(culture_image, (600, 400), Image.Resampling.LANCZOS)

    col1, col2 = st.columns(2)

    with col1:
        st.image(art_image_resized, caption="**Art Forms of India**", use_container_width=True)
        left, center, right = st.columns([1, 1, 1])
        with center:
            if st.button("View Different Art forms of India", key="art_btn"):
                st.session_state.active_tab = "art"
                st.markdown('<script>scrollToSection("art-section")</script>', unsafe_allow_html=True)

    with col2:
        st.image(culture_image_resized, caption="**Cultural Experiences in India**", use_container_width=True)
        left, center, right = st.columns([1, 1, 1])
        with center:
            if st.button("Explore the Cultural Experiences of India", key="culture_btn"):
                st.session_state.active_tab = "culture"
                st.markdown('<script>scrollToSection("culture-section")</script>', unsafe_allow_html=True)


    # Render Sections
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = ""

    if st.session_state.active_tab == "art":
        st.markdown("---")
        render_artforms_section(df_artforms)
    elif st.session_state.active_tab == "culture":
        st.markdown("---")
        render_experiences_section(df_experiences)

    st.markdown("---")
    st.markdown("## UNESCO identified tangible world heritage sites in India")
    left, center, right = st.columns([2,5,2])
    with center:
        st.image("images/unesco_heritage.jpg","",use_container_width=True )

    st.markdown('</div>', unsafe_allow_html=True)
