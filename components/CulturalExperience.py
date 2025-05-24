import streamlit as st
import os
import base64
import streamlit.components.v1 as components

def render_experiences_section(df_experiences):
    st.header("Immersive Cultural Experiences")

    carousel_items = ""
    for _, row in df_experiences.iterrows():
        activity = row.get("ACTIVITY", "Unknown")
        place = row.get("PLACE", "Unknown")
        category = row.get("CATEGORY", "General")
        description = row.get("DESCRIPTION", "No description available.")
        image = row.get("IMAGE_URL", None)

        if not image:
            continue

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

    if not carousel_items:
        st.info("No cultural experiences found or images missing.")
        return

    # Final HTML block
    html_code = f"""
    <style>
        .carousel-wrapper {{
            position: relative;
            width: 100%;
            max-width: 930px;
            margin: auto;
            overflow: hidden;
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
            const itemWidth = 900 + 32;
            currentIndex += direction;
            if (currentIndex < 0) currentIndex = 0;
            if (currentIndex >= totalItems) currentIndex = totalItems - 1;
            track.style.transform = 'translateX(' + (-itemWidth * currentIndex) + 'px)';
        }}
    </script>
    """

    components.html(html_code, height=450)
