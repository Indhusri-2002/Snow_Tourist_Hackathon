import streamlit as st
import pandas as pd
import os
import base64

IMAGE_DIR = "images/art_forms"

def render_artforms_section(df_artforms):
    st.markdown('<a name="art-section"></a>', unsafe_allow_html=True)
    st.header("Traditional Art Forms of India")

    # Filters
    unique_states = sorted(df_artforms["STATE"].dropna().unique())
    unique_types = sorted(df_artforms["TYPE_OF_ARTFORM"].dropna().unique()) 

    state_col, type_col = st.columns(2)

    with state_col:
        selected_state = st.selectbox("Filter by State", ["All"] + unique_states)

    with type_col:
        selected_type = st.selectbox("Filter by Type", ["All"] + unique_types)

    # Apply filters
    filtered_df = df_artforms.copy()
    if selected_state != "All":
        filtered_df = filtered_df[filtered_df["STATE"] == selected_state]
    if selected_type != "All":
        filtered_df = filtered_df[filtered_df["TYPE_OF_ARTFORM"] == selected_type]

    # CSS for card layout
    st.markdown("""
        <style>
            .art-card {
                height: 380px;
                padding: 10px;
                border-radius: 10px;
                overflow: hidden;
                margin-bottom: 18px;
                box-shadow: 0 0 8px rgba(0,0,0,0.2);
            }
            .card-img {
                width: 100%;
                height: 180px;
                object-fit: cover;
                border-radius: 8px;
                margin-bottom: 8px;
            }
            .no-image {
                height: 180px;
                width: 100%;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #666;
                font-size: 1rem;
                margin-bottom: 8px;
            }
            .art-card-title {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 4px;
            }
            .art-card-meta {
                font-size: 14px;
                margin-bottom: 6px;
            }
            .art-card-desc {
                font-size: 13px;
                overflow: auto;
                max-height: 140px;
            }

             @media (prefers-color-scheme: dark) {
                .art-card {
                    box-shadow: 0 0 8px rgba(255,255,255,0.2);
                }
             }
        </style>
    """, unsafe_allow_html=True)

    # Display in 4 columns
    cols = st.columns(4)
    artforms_split = [filtered_df.iloc[i::4] for i in range(4)]

    for col, df_split in zip(cols, artforms_split):
        with col:
            for _, row in df_split.iterrows():
                art_form = row["ART_FORM"]
                state = row["STATE"]
                description = row["DESCRIPTION"]
                image_file = f"{art_form}.jpg"
                image_path = os.path.join(IMAGE_DIR, image_file)

                try:
                    with open(image_path, "rb") as img_file:
                        img_base64 = base64.b64encode(img_file.read()).decode()
                        image_tag = f'<img src="data:image/jpeg;base64,{img_base64}" class="card-img">'
                except:
                    image_tag = '<div class="no-image">No Image</div>'

                st.markdown(f"""
                    <div class="art-card">
                        {image_tag}
                        <div class="art-card-title">{art_form}</div>
                        <div class="art-card-meta"><strong>State:</strong> {state}</div>
                        <div class="art-card-desc">{description}</div>
                    </div>
                """, unsafe_allow_html=True)
