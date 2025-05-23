import streamlit as st
import pandas as pd
import os
from PIL import Image, ImageOps
from services.snowflake_connector import get_snowflake_connection
import base64
import streamlit.components.v1 as components

# Cache DB calls for 10 minutes
@st.cache_data(ttl=600)
def load_art_and_experience_data():
    conn = get_snowflake_connection()
    try:
        df_artforms = pd.read_sql("SELECT * FROM STAGE.STG_ARTFORMS_OF_INDIA", conn)
        df_experiences = pd.read_sql("SELECT * FROM STAGE.STG_CULTURAL_EXPERIENCES", conn)
    finally:
        conn.close()
    return df_artforms, df_experiences

def render_image_card(image_path, width=300, height=200):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image_resized = ImageOps.fit(image, (width, height), Image.Resampling.LANCZOS)
        st.image(image_resized)
    else:
        st.warning(f"Image not found: `{image_path}`")

def render_artforms_section(df_artforms):
    import streamlit as st

    st.markdown('<a name="art-section"></a>', unsafe_allow_html=True)
    st.header("Traditional Art Forms of India")

    # Assuming df_artforms has a "TYPE" column - adjust if needed
    unique_states = sorted(df_artforms["STATE"].dropna().unique())
    unique_types = sorted(df_artforms["TYPE_OF_ARTFORM"].dropna().unique()) 

    # Filter dropdowns
    state_col, type_col = st.columns(2)

    with state_col:
        selected_state = st.selectbox("Filter by State", ["All"] + unique_states)

    with type_col:
        if unique_types:
            selected_type = st.selectbox("Filter by Type", ["All"] + unique_types)
        else:
            selected_type = None

    # Apply filters
    filtered_df = df_artforms.copy()
    if selected_state != "All":
        filtered_df = filtered_df[filtered_df["STATE"] == selected_state]
    if selected_type and selected_type != "All":
        filtered_df = filtered_df[filtered_df["TYPE_OF_ARTFORM"] == selected_type]

    # 4 columns layout
    cols = st.columns(4)

    # Split data into 4 groups for the 4 columns (round robin)
    artforms_split = [filtered_df.iloc[i::4] for i in range(4)]

    for col, df_split in zip(cols, artforms_split):
        with col:
            for _, row in df_split.iterrows():
                art_form = row["ART_FORM"]
                state = row["STATE"]
                description = row["DESCRIPTION"]
                image_path = f"images/art_forms/{art_form}.jpg"

                with st.container():
                    # Show image first (you can control size via render_image_card or st.image)
                    render_image_card(image_path)

                    # Then show details below
                    st.markdown(f"### {art_form}")
                    st.markdown(f"**State:** {state}")
                    st.markdown(f"**Description:**")
                    st.markdown(description)

                    st.markdown("---")



import streamlit as st
import streamlit.components.v1 as components
import os
import base64

def render_experiences_section(df_experiences):
    st.header("Immersive Cultural Experiences")

    # Build carousel items
    carousel_items = ""
    for _, row in df_experiences.iterrows():
        activity = row["ACTIVITY"]
        place = row["PLACE"]
        category = row["CATEGORY"]
        description = row["DESCRIPTION"]
        image = row["IMAGE_URL"]
        image_path = f"images/cultural_experiences/{image}.jpg"

        if not os.path.exists(image_path):
            continue

        with open(image_path, "rb") as img_file:
            b64_image = base64.b64encode(img_file.read()).decode()

        item_html = f"""
        <div class="carousel-item">
            <div class="carousel-image">
                <img src="data:image/jpeg;base64,{b64_image}" alt="{activity}" />
            </div>
            <div class="carousel-text">
                <h4>{activity} in {place}</h4>
                <p><b>Category:</b> {category}</p>
                <p>{description}</p>
            </div>
        </div>
        """
        carousel_items += item_html

    # Final HTML
    html_code = f"""
    <style>
        .carousel-wrapper {{
            position: relative;
            width: 930px;
            margin: 0 auto;
            overflow: hidden;
            align-items: center;
        }}
        .carousel-track {{
            display: flex;
            transition: transform 0.5s ease;
        }}
        .carousel-item {{
            display: flex;
            width: 900px;
            height: 400px;
            margin: 0 16px;
            background: #faf9f6;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            overflow: hidden;
            flex-shrink: 0;
        }}
        .carousel-image {{
            flex: 70%;
        }}
        .carousel-image img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .carousel-text {{
            flex: 30%;
            padding: 1rem;
            overflow-y: auto;
        }}
        .carousel-button {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 1.5rem;
            cursor: pointer;
            z-index: 1;
        }}
        .left-arrow {{
            left: 0;
        }}
        .right-arrow {{
            right: 0;
        }}
    </style>
    <div class="carousel-wrapper">
        <button class="carousel-button left-arrow" onclick="moveSlide(-1)">❮</button>
        <div class="carousel-track" id="carouselTrack">
            {carousel_items}
        </div>
        <button class="carousel-button right-arrow" onclick="moveSlide(1)">❯</button>
    </div>
    <script>
        let currentIndex = 0;
        const track = document.getElementById('carouselTrack');
        const totalItems = document.querySelectorAll('.carousel-item').length;
        function moveSlide(direction) {{
            const itemWidth = 900 + 32; // width + margin
            currentIndex += direction;
            if (currentIndex < 0) currentIndex = 0;
            if (currentIndex >= totalItems) currentIndex = totalItems - 1;
            track.style.transform = 'translateX(' + (-itemWidth * currentIndex) + 'px)';
        }}
    </script>
    """

    components.html(html_code, height=420)

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
    df_artforms, df_experiences = load_art_and_experience_data()

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
