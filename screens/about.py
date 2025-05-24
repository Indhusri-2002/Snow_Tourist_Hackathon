import streamlit as st
from PIL import Image
import pandas as pd
import folium
from streamlit_folium import st_folium
from components.UntouchedPlaces import untouched_places
from components.PlacesToVisit import places_to_visit
from utils.data_loader import load_datasets

def render():

    dfs = load_datasets()
    df_places_to_visit = dfs['places_to_visit']
    df_untouched = dfs['untouched_places']

    st.markdown("""
    <style>
    .header-section {
        animation: fadeIn 1.2s ease-in-out forwards;
        opacity: 0;
        padding: 20px;
        border-radius: 12px;
        background-color: transparent;
        color: #fff;
        # background: #99daff;
        # background: linear-gradient(90deg,rgba(153, 218, 255, 1) 0%, rgba(196, 231, 255, 1) 50%, rgba(176, 227, 255, 1) 100%);
        box-shadow: 0 4px 10px rgba(255,255,255,0.3);
        margin-top: 20px;
        margin-bottom: 20px;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }

    .header-section h1 {
        font-size: 2.4em;
        color: #0a48b2;
        margin-bottom: 10px;
    }

    .typewriter {
        overflow: hidden;
        border-right: .15em solid #777;
        white-space: nowrap;
        margin: 0 auto 20px auto;
        letter-spacing: .05em;
        animation: typing 4s steps(60, end), blink-caret 0.75s step-end infinite;
        font-style: italic;
        color: #777;
        font-size: 1.2em;
        width: 100%;
        max-width: 650px;
    }

    /* Text content section */
    .content-section {
        animation: fadeIn 1.5s ease-in-out forwards;
        opacity: 0;
        padding: 20px;
        background-color: transparent;
        border-radius: 12px;
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
        font-size: 1.05em;
        line-height: 1.2;
        box-shadow: 0 4px 10px rgba(255,255,255,0.3);
        display: flex;
        flex-direction: column;
    }

    /* Animations */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #fff }
    }
    </style>

    <!-- Header Section -->
    <div class="header-section">
        <h1>Responsible Tourism in India</h1>
        <div class="typewriter">"Travel with respect. Travel with purpose. Discover India sustainably."</div>
    </div>

    <!-- Content Section -->
    <div class="content-section">
        <p>Responsible tourism is about <strong>making mindful choices</strong> that preserve the environment, 
        respect cultural traditions, and empower local communities.</p>
        <p>Whether you're trekking in the Himalayas, relaxing on a coastal beach, or exploring desert heritage —
        <strong>how</strong> you travel matters.</p>
        <p>🌍 By traveling responsibly, you become more than a tourist — 
        <em>you become a positive force for sustainability and inclusion.</em></p>
    </div>
    """, unsafe_allow_html=True)




    st.markdown("""
    <style>
    .tip-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 16px;
        margin-top: 20px;
    }

    .tip-box {
        flex: 1 1 calc(48% - 10px);
        display: flex;
        align-items: center;
        border-radius: 12px;
        padding: 12px 16px;
        background-color: transparent;
        box-shadow: 0 4px 10px rgba(255,255,255,0.3);
        color: #fff;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        opacity: 0;
        animation: fadeInUp 0.6s ease forwards;
        animation-fill-mode: forwards;
        margin-bottom: 10px;
    }

    .tip-box:nth-child(1) { animation-delay: 0s; }
    .tip-box:nth-child(2) { animation-delay: 0.1s; }
    .tip-box:nth-child(3) { animation-delay: 0.2s; }
    .tip-box:nth-child(4) { animation-delay: 0.3s; }
    .tip-box:nth-child(5) { animation-delay: 0.4s; }
    .tip-box:nth-child(6) { animation-delay: 0.5s; }

    .tip-box:hover {
        transform: scale(1.03);
        box-shadow: 0 4px 10px rgba(255,255,255,0.3);
    }

    .tip-icon {
        font-size: 32px;
        margin-right: 15px;
    }

    .tip-text {
        font-size: 16px;
        color: #fff;
    }

    /* Animation */
    @keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Responsive */
    @media (max-width: 768px) {
        .tip-box {
            flex: 1 1 100%;
        }
    }
    </style>

    <div class="tip-container">
        <div class="tip-box">
            <div class="tip-icon">🧭</div>
            <div class="tip-text"><strong>Respect Local Traditions</strong> – Be culturally aware; ask before taking photos, dress appropriately, and follow community norms.</div>
        </div>
        <div class="tip-box">
            <div class="tip-icon">🌿</div>
            <div class="tip-text"><strong>Reduce Environmental Impact</strong> – Carry reusables, avoid littering, and steer clear of plastic pollution.</div>
        </div>
        <div class="tip-box">
            <div class="tip-icon">🚉</div>
            <div class="tip-text"><strong>Use Sustainable Transport</strong> – Opt for public transport, shared rides, or non-motorized travel like walking and cycling.</div>
        </div>
        <div class="tip-box">
            <div class="tip-icon">🛍️</div>
            <div class="tip-text"><strong>Support Local Economies</strong> – Prefer small-scale local businesses, artisans, and cooperatives over large chains.</div>
        </div>
        <div class="tip-box">
            <div class="tip-icon">🐾</div>
            <div class="tip-text"><strong>Avoid Harmful Attractions</strong> – Skip wildlife shows, elephant rides, or any activity that exploits animals or people.</div>
        </div>
        <div class="tip-box">
            <div class="tip-icon">🚯</div>
            <div class="tip-text"><strong>Leave No Trace</strong> – Respect all places — natural or cultural — by preserving their beauty and cleanliness.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("---")
    
    # places to visit
    places_to_visit(df_places_to_visit)

    st.markdown("---")

    # Untouched Places
    untouched_places(df_untouched)