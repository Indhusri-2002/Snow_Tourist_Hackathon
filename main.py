import streamlit as st
from screens import home, analytics, about

st.set_page_config(page_title="India Tourism Dashboard", layout="wide")

st.markdown("""
    <style>
    .stTabs [role="tab"] {
        padding: 14px 30px;
        color: #444;
        background-color: #f0f0f0;
        border: none;
        border-radius: 8px;
        box-shadow: none;
    }

    /* Hover effect */
    .stTabs [role="tab"]:hover {
        background-color: #e0e0e0;
        color: #000;
    }

    /* Selected tab styling */
    .stTabs [aria-selected="true"] {
        background-color: #FF4B4B !important;
        color: white !important;
        font-weight: bold;
        border-bottom: none !important;
        box-shadow: none !important;
    }

    .st-ar {
        justify-content: center !important;
        gap:20px;
    }
    .st-c7 {
        display:none !important; 
    }
    .st-emotion-cache-qoz3f2.erovr380 p {
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)




tab = st.tabs(["Explore India", "Tourism Insights", "Undiscovered India"])

with tab[0]:
    home.render()
with tab[1]:
    analytics.render()
with tab[2]:
    about.render()


# Hide Streamlit's default footer
hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)

# Custom Footer with f-string
custom_footer = f"""
    <style>
    .custom-footer {{
        width: 100%;
        text-align: center;
        padding: 12px 16px;
        font-size: 13px;
        z-index: 100;
        line-height: 1.6;
    }}
    .logo-img {{
        height: 14px;
        vertical-align: middle;
        margin: 0 4px;
    }}
    .custom-footer a {{
        color: #66b2ff;
        text-decoration: none;
        margin: 0 4px;
    }}
    .custom-footer a:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="custom-footer">
      <div>
        Made with ❤️ using Streamlit and ❄️ Snowflake | 💻 Best on Desktop | 🌙 Dark Mode preferred
      </div>
      <div>
        Feedback? - 📧 : 
        <a href="mailto:akanth24@gmail.com">akanth24@gmail.com</a>, 
        <a href="mailto:kodatiindhusri@gmail.com">kodatiindhusri@gmail.com</a>, 
        <a href="mailto:avinashyerra123@gmail.com">avinashyerra123@gmail.com</a>
      </div>
    </div>
"""

st.markdown(custom_footer, unsafe_allow_html=True)