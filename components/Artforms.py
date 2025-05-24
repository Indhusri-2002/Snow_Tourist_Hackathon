import streamlit as st
import pandas as pd
import os
from components.ImageCard import render_image_card


def render_artforms_section(df_artforms):
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
