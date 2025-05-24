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

    html_code = f"""
    <style>
        .carousel-wrapper {{
            position: relative;
            width: 100%;
            max-width: 960px;
            margin: 5rem auto 2rem;
            overflow: hidden;
        }}
        .carousel-track {{
            display: flex;
            transition: transform 0.5s ease-in-out;
        }}
        .carousel-item {{
            display: flex;
            flex-direction: row;
            width: 928px;
            height: 400px;
            margin: 0 16px;
            background-color: #faf9f6;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            flex-shrink: 0;
            overflow: hidden;
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
            background-color: rgba(0, 0, 0, 0.4);
            color: white;
            border: none;
            padding: 0.75rem 1rem;
            font-size: 2rem;
            cursor: pointer;
            z-index: 10;
            border-radius: 8px;
        }}
        .left-arrow {{
            left: 8px;
        }}
        .right-arrow {{
            right: 8px;
        }}
        @media (prefers-color-scheme: dark) {{
            .carousel-item {{
                background: #1f1f1f;
                color: #f0f0f0;
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            }}
            .carousel-button {{
                background-color: rgba(255, 255, 255, 0.3);
            }}
            .carousel-text {{
                color: #e0e0e0;
            }}
        }}
        @media (max-width: 960px) {{
            .carousel-item {{
                flex-direction: column;
                height: auto;
                width: 90%;
                margin: 0 auto;
            }}
            .carousel-image {{
                flex: none;
                height: 200px;
            }}
            .carousel-text {{
                flex: none;
                height: auto;
            }}
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
            const itemWidth = 960;
            currentIndex += direction;
            if (currentIndex < 0) currentIndex = 0;
            if (currentIndex >= totalItems) currentIndex = totalItems - 1;
            track.style.transform = 'translateX(' + (-itemWidth * currentIndex) + 'px)';
        }}
    </script>
    """

    components.html(html_code, height=500)
