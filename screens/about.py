import streamlit as st
from PIL import Image
import pandas as pd
import folium
from streamlit_folium import st_folium
from components.UntouchedPlaces import untouched_places

def render():
    # --- Hero Section with Text Left & Image Right ---

    st.markdown("""
    <style>
    .header-section {
        animation: fadeIn 1.2s ease-in-out forwards;
        opacity: 0;
        padding: 20px;
        border-radius: 12px;
        background-color: #e3f4fc;
        color: #333;
        background: linear-gradient(90deg,rgba(250, 255, 240, 1) 0%, rgba(173, 213, 255, 1) 50%, rgba(232, 255, 232, 1) 100%);
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
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
        background-color: #e3f4fc;
        border-radius: 12px;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
        font-size: 1.05em;
        line-height: 1.6;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        display: flex;
        flex-direction: column;
        gap:10px;
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
        50% { border-color: #333 }
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
        border: 1px solid #444;
        border-radius: 12px;
        padding: 12px 16px;
        background-color: #e3f4fc;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        color: #333;
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
        box-shadow: 4px 4px 12px rgba(0,0,0,0.3);
    }

    .tip-icon {
        font-size: 32px;
        margin-right: 15px;
    }

    .tip-text {
        font-size: 16px;
        color: #333;
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
    st.header("📍 State-wise Responsible Destinations")

    # --- Destination data ---
    destinations = [
        {
            "title": "Sikkim – India's First Organic State",
            "desc": (
                "Sikkim is India's first fully organic state, known for eco-friendly farming and a ban on single-use plastics. "
                "Terraced farms, monasteries, and local homestays highlight its natural beauty and sustainable tourism."
            ),
            "img": "images/sikkim.jpg",
            "link": "https://sikkimtourism.gov.in",
            "location": "https://www.google.com/maps/place/Sikkim"
        },
        {
            "title": "Mawlynnong, Meghalaya – Asia's Cleanest Village",
            "desc": (
                "Nicknamed 'God’s Own Garden', Mawlynnong is famous for its cleanliness and plastic-free policies. "
                "Visitors enjoy bamboo skywalks, stone paths, and eco-conscious homestays."
            ),
            "img": "images/mawlynnong.jpg",
            "link": "https://www.meghalayatourism.in",
            "location": "https://www.google.com/maps/place/Mawlynnong"
        },
        {
            "title": "Thenmala, Kerala – India’s First Eco-Tourism Hub",
            "desc": (
                "Thenmala offers forest treks, tree huts, and cultural shows while preserving the Western Ghats ecosystem. "
                "Trained local guides enhance the eco-tourism experience."
            ),
            "img": "images/thenmala.jpeg",
            "link": "https://www.thenmalaecotourism.com",
            "location": "https://www.google.com/maps/place/Thenmala"
        },
        {
            "title": "Khonoma, Nagaland – Conservation Village",
            "desc": (
                "This Angami tribal village has banned hunting and created its own wildlife sanctuary. "
                "Visitors experience traditional lifestyles and serene, green landscapes."
            ),
            "img": "images/khonoma.jpg",
            "link": "https://tourism.nagaland.gov.in",
            "location": "https://www.google.com/maps/place/Khonoma"
        },
        {
            "title": "Majuli, Assam – World’s Largest River Island",
            "desc": (
                "Majuli blends culture and ecology with satras, mask-making, and wetland conservation. "
                "Eco-stays and artisan interaction enrich this island visit."
            ),
            "img": "images/majuli.jpg",
            "link": "https://tourism.assam.gov.in/portlets/majuli",
            "location": "https://www.google.com/maps/place/Majuli"
        },
        {
            "title": "Matheran, Maharashtra – India's Car-Free Hill Station",
            "desc": (
                "Matheran is free of motor vehicles, offering clean air and scenic trails. "
                "Explore by foot, horseback, or toy train for a peaceful eco-retreat."
            ),
            "img": "images/matheran.jpeg",
            "link": "https://www.maharashtratourism.gov.in",
            "location": "https://www.google.com/maps/place/Matheran"
        },
        {
            "title": "Channapatna, Karnataka – Town of Toy Makers",
            "desc": (
                "Known for handcrafted wooden toys, Channapatna promotes sustainable crafts and artisan livelihoods. "
                "Tourists can explore workshops and shop for eco-friendly souvenirs."
            ),
            "img": "images/channapatna.jpg",
            "link": "https://karnatakatourism.org/tour-item/channapatna",
            "location": "https://www.google.com/maps/place/Channapatna"
        },
        {
            "title": "Spiti Valley, Himachal Pradesh – High-Altitude Sustainability",
            "desc": (
                "Spiti promotes eco-lodges, solar-powered homes, and mindful trekking. "
                "Travelers immerse in Himalayan life while supporting conservation."
            ),
            "img": "images/spiti.jpeg",
            "link": "https://himachaltourism.gov.in",
            "location": "https://www.google.com/maps/place/Spiti+Valley"
        },
        {
            "title": "Araku Valley, Andhra Pradesh – Tribal Eco-Tourism",
            "desc": (
                "Home to tribal communities and coffee plantations, Araku offers guided cultural tours and eco-stays. "
                "Tourism supports local heritage and sustainability."
            ),
            "img": "images/araku.jpg",
            "link": "https://tourism.ap.gov.in",
            "location": "https://www.google.com/maps/place/Araku+Valley"
        },
        {
            "title": "Ramnagar, Uttarakhand – Gateway to Wildlife Conservation",
            "desc": (
                "Base for Jim Corbett National Park, Ramnagar promotes wildlife awareness through eco-resorts and guided safaris. "
                "Tourism supports tiger conservation and local culture."
            ),
            "img": "images/ramnagar.jpeg",
            "link": "https://uttarakhandtourism.gov.in",
            "location": "https://www.google.com/maps/place/Ramnagar"
        },
        {
            "title": "Auroville, Tamil Nadu – Experimental Sustainable Township",
            "desc": (
                "Auroville is dedicated to sustainability, with organic farms, renewable energy, and eco-architecture. "
                "Visitors join workshops and conscious living programs."
            ),
            "img": "images/auroville.jpeg",
            "link": "https://auroville.org",
            "location": "https://www.google.com/maps/place/Auroville"
        },
        {
            "title": "Bhuj, Gujarat – Post-Disaster Craft Revival",
            "desc": (
                "Bhuj revived its economy post-earthquake through crafts like Bandhani and embroidery. "
                "Homestays and artisan tours support cultural resilience and local livelihoods."
            ),
            "img": "images/bhuj.jpg",
            "link": "https://www.gujarattourism.com",
            "location": "https://www.google.com/maps/place/Bhuj"
        }
    ]


    lat_lon = {
        "Sikkim – India's First Organic State": [27.317, 88.606],
        "Mawlynnong, Meghalaya – Asia's Cleanest Village": [25.200, 92.018],
        "Thenmala, Kerala – India’s First Eco-Tourism Hub": [8.943, 77.110],
        "Khonoma, Nagaland – Conservation Village": [25.667, 94.000],
        "Majuli, Assam – World’s Largest River Island": [27.000, 94.222],
        "Matheran, Maharashtra – India's Car-Free Hill Station": [18.985, 73.272],
        "Channapatna, Karnataka – Town of Toy Makers": [12.655, 77.284],
        "Spiti Valley, Himachal Pradesh – High-Altitude Sustainability": [32.246, 78.033],
        "Araku Valley, Andhra Pradesh – Tribal Eco-Tourism": [18.328, 82.868],
        "Ramnagar, Uttarakhand – Gateway to Wildlife Conservation": [29.392, 79.126],
        "Auroville, Tamil Nadu – Experimental Sustainable Township": [12.005, 79.808],
        "Bhuj, Gujarat – Post-Disaster Resilience and Craft Revival": [23.250, 69.667]
    }


    m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)

    for dest in destinations:
        if dest["title"] in lat_lon:
            lat, lon = lat_lon[dest["title"]]
            
            # Create an HTML popup with clickable link
            html = f'''
                <div>
                    <a href="{dest["location"]}" target="_blank" style="text-decoration:none; color:#0a48b2;">
                        {dest["title"]}
                    </a>
                </div>
            '''
            iframe = folium.IFrame(html=html, width=250, height=50)
            popup = folium.Popup(iframe, max_width=300)

            folium.Marker(
                location=[lat, lon],
                popup=popup,
                tooltip=dest["title"],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)

    
    # --- Display the map in Streamlit ---
    st.subheader("🗺️ Explore Destinations on Interactive Map")
    # --- Center the map using columns ---
    left, center, right = st.columns([1, 3, 1])
    with center:
        st_folium(m, width=800, height=600)

   # Set initial visibility limit
    VISIBLE_COUNT = 4

    # Session state to store how many destinations are currently visible
    if 'visible_count' not in st.session_state:
        st.session_state.visible_count = VISIBLE_COUNT

    # Function to display destinations in 2-column layout
    def display_destinations(dest_list):
        for i in range(0, len(dest_list), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(dest_list):
                    dest = dest_list[i + j]
                    with cols[j]:
                        st.subheader(dest['title'])
                        st.image(dest["img"], width=500)
                        st.markdown(
                            f'<span style="display:flex; gap:10px;">'
                            f'<a href="{dest["link"]}" target="_blank">🔗 Official Tourism Site</a>'
                            f'<a href="{dest["location"]}" target="_blank">🗺️ Google Maps</a>'
                            f'</span>',
                            unsafe_allow_html=True
                        )
                        st.write(dest["desc"])
            st.markdown("---")

    # Display visible destinations
    display_destinations(destinations[:st.session_state.visible_count])

    # Show "View More" button if there are more destinations to show
    if st.session_state.visible_count < len(destinations):
        if st.button("View More"):
            st.session_state.visible_count += VISIBLE_COUNT


    # UNTOUCHED PLACES
    untouched_places()



