import os
import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from streamlit_folium import st_folium
from components.ImageCard import render_image_card


# Constants
MAP_CENTER = [22.9734, 78.6569]
MAP_ZOOM = 5
IMAGE_DIR = "images/untouched_places"

def untouched_places(df_untouched):
    st.title("Untouched Places in India")

    # Dropdown filter
    selected_place = st.selectbox("Select a place", ["All"] + df_untouched["PLACE"].unique().tolist())

    df_filtered = df_untouched if selected_place == "All" else df_untouched[df_untouched["PLACE"] == selected_place]

    if df_filtered.empty:
        st.warning("No data available for the selected place.")
        return

    # Create the map
    m = folium.Map(location=MAP_CENTER, zoom_start=MAP_ZOOM)
    for _, row in df_filtered.iterrows():
        place = row["PLACE"]
        lat = row["LAT"]
        lon = row["LON"]
        link = row["LINK_URL"]

        popup_html = f"<b>{place}</b><br><a href='{link}' target='_blank'>Open in Google Maps</a>"
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=place,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

    

    if selected_place != "All":
        # Show map and details side by side
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("Map View")
            st_folium(m, width=600, height=500)
        with col2:
            row = df_filtered.iloc[0]
            place = row["PLACE"]
            state = row["STATE_UT"]
            reason = row["REASON"]
            season = row["BEST_SEASON"]
            link = row["LINK_URL"]
            image_file = f"{place.lower().replace(' ', '_')}.jpeg"
            image_path = os.path.join(IMAGE_DIR, image_file)

            st.subheader(f"{place} ({state})")
            render_image_card(image_path,500,330)
            st.write(f"**Reason:** {reason}")
            st.write(f"**Best Season:** {season}")
            st.markdown(f"[Open in Google Maps]({link})")

    else:
        # Map on top, horizontal card scroll below
        st.subheader("Map View")
        st_folium(m, width=700, height=500)

        card_html = ""
        for _, row in df_filtered.iterrows():
            place = row["PLACE"]
            state = row["STATE_UT"]
            reason = row["REASON"]
            season = row["BEST_SEASON"]
            link = row["LINK_URL"]
            image_file = f"{place.lower().replace(' ', '_')}.jpeg"
            image_path = os.path.join(IMAGE_DIR, image_file)

            try:
                with open(image_path, "rb") as img_file:
                    img_base64 = base64.b64encode(img_file.read()).decode()
                    image_tag = f'<img src="data:image/jpeg;base64,{img_base64}" class="card-img">'
            except:
                image_tag = '<div class="no-image">No Image</div>'

            card_html += f"""
            <div class="card">
                {image_tag}
                <div class="card-content">
                    <h4>{place} ({state})</h4>
                    <p><b>Reason:</b> {reason}</p>
                    <p><b>Best Season:</b> {season}</p>
                    <a href="{link}" target="_blank">Open in Google Maps</a>
                </div>
            </div>
            """

        # Final scrollable section
        full_html = f"""
        <style>
        .scroll-container {{
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            gap: 1rem;
            padding: 1rem 0;
        }}

        .card {{
            min-width: 350px;
            max-width: 350px;
            flex-shrink: 0;
            border-radius: 12px;
            scroll-snap-align: start;
            padding: 12px;
            background-color: #f8f8f8;
            color: #000000;
            box-shadow: 0 0 8px rgba(0,0,0,0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeInUp 0.8s ease forwards;
            opacity: 0;
            transform: translateY(20px);
        }}

        .card:hover {{
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }}

        .card-img {{
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
        }}

        .card-content {{
            padding-top: 10px;
        }}

        .no-image {{
            height: 180px;
            background-color: #ddd;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            color: #555;
        }}

        @media (prefers-color-scheme: dark) {{
            .card {{
                background-color: #000;
                color: #fff;
                box-shadow: 0 0 8px rgba(255, 255, 255, 0.3);
            }}
            .card:hover {{
                box-shadow: 0 8px 25px rgba(255, 255, 255, 0.3);
            }}
            .no-image {{
                background-color: #333;
                color: #ccc;
            }}
        }}

        @keyframes fadeInUp {{
            0% {{
                opacity: 0;
                transform: translateY(20px);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        </style>

        <div class="scroll-container">
            {card_html}
        </div>
        """


        components.html(full_html, height=520, scrolling=True)
