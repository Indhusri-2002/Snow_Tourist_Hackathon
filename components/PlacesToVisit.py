import streamlit as st
import folium
from streamlit_folium import st_folium
from components.ImageCard import render_image_card


def places_to_visit(df_places_to_visit):
    st.header("State-wise Responsible Places to Visit")

    # Create map centered on India
    m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)

    # Add markers for each place
    for _, place in df_places_to_visit.iterrows():
        lat = place['LAT']
        lon = place['LONG']
        title = place['TITLE']
        location_url = place['LOCATION']

        html = f'''
            <div>
                <a href="{location_url}" target="_blank" style="text-decoration:none; color:#0a48b2;">
                    {title}
                </a>
            </div>
        '''
        iframe = folium.IFrame(html=html, width=250, height=50)
        popup = folium.Popup(iframe, max_width=300)

        folium.Marker(
            location=[lat, lon],
            popup=popup,
            tooltip=title,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # Display the map centered in the layout
    left, center, right = st.columns([1, 3, 1])
    with center:
        st_folium(m, width=800, height=600)

    # Limit visible destinations
    VISIBLE_COUNT = 4
    if "visible_count" not in st.session_state:
        st.session_state.visible_count = VISIBLE_COUNT

    def display_destinations(dest_df):
        for i in range(0, len(dest_df), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(dest_df):
                    dest = dest_df.iloc[i + j]
                    with cols[j]:
                        st.subheader(f"{dest['TITLE']} – {dest['STATE']}")
                        
                        img_url = dest['IMG']
                        render_image_card(img_url,600,400)

                        st.markdown(
                            f'''
                            <span style="display:flex; gap:10px; flex-wrap:wrap;">
                                <a href="{dest['LINK']}" target="_blank">🔗 Official Tourism Site</a>
                                <a href="{dest['LOCATION']}" target="_blank">🗺️ Google Maps</a>
                            </span>
                            ''',
                            unsafe_allow_html=True
                        )
                        st.write(dest["DESC"])
            st.markdown("---")

    # Display initial destinations
    display_destinations(df_places_to_visit[:st.session_state.visible_count])

    # "View More" logic
    if st.session_state.visible_count < len(df_places_to_visit):
        if st.button("View More"):
            st.session_state.visible_count += VISIBLE_COUNT
