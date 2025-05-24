import os
import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from streamlit_folium import st_folium
from utils.data_loader import load_datasets

# Map center
map_center = [22.9734, 78.6569]  # India centroid
map_zoom = 5

def untouched_places():
    st.title("Untouched Places in India")

    dfs = load_datasets()
    df_untouched = dfs['untouched_places']

    selected_place = st.selectbox("Select a place", ["All"] + df_untouched["PLACE"].unique().tolist())

    if selected_place != "All":
        df_filtered = df_untouched[df_untouched["PLACE"] == selected_place]
    else:
        df_filtered = df_untouched

    if df_filtered.empty:
        st.warning("No data available for the selected place.")
        return

    # Create map
    m = folium.Map(location=map_center, zoom_start=map_zoom)
    for _, row in df_filtered.iterrows():
        place = row["PLACE"]
        lat = row['LAT']
        lon = row['LON']
        link = row['LINK_URL']
        
        popup_html = f"<b>{place}</b><br><a href='{link}' target='_blank'>Open in Google Maps</a>"
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=place,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

    st.subheader("Map View")

    if selected_place != "All":
        # Side-by-side layout
        col1, col2 = st.columns([1, 1])
        with col1:
            st_folium(m, width=600, height=500)
        with col2:
            row = df_filtered.iloc[0]
            place = row["PLACE"]
            state = row["STATE_UT"]
            reason = row["REASON"]
            season = row["BEST_SEASON"]
            image_path = f"images/untouched_places/{place.lower().replace(' ', '_')}.jpeg"
            link = row["LINK_URL"]

            st.markdown(f"### {place} ({state})")
            if os.path.exists(image_path):
                st.image(image_path, width=500)
            else:
                st.info("No image available")
            st.write(f"**Reason:** {reason}")
            st.write(f"**Best Season:** {season}")
            st.markdown(f"[Open in Google Maps]({link})")
    else:
        # Show map then carousel
        st_folium(m, width=700, height=500)

        card_html = ""

        for _, row in df_filtered.iterrows():
            place = row["PLACE"]
            state = row["STATE_UT"]
            reason = row["REASON"]
            season = row["BEST_SEASON"]
            image_path = f"images/untouched_places/{place.lower().replace(' ', '_')}.jpeg"
            link = row["LINK_URL"]

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
            background: #e3f4fc;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            scroll-snap-align: start;
            padding: 10px;
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
            background-color: #eee;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666;
        }}
        </style>

        <div class="scroll-container">
            {card_html}
        </div>
        """

        components.html(full_html, height=500, scrolling=True)
