import os
from PIL import Image, ImageOps
import streamlit as st

def render_image_card(image_path, width=300, height=200):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image_resized = ImageOps.fit(image, (width, height), Image.Resampling.LANCZOS)
        st.image(image_resized)
    else:
        st.warning(f"Image not found: `{image_path}`")