import streamlit as st
from PIL import Image
import pandas as pd
import folium
from streamlit_folium import st_folium


def render():
    # --- Hero Section with Text Left & Image Right ---
    st.title("🌿 Responsible Tourism in India")
    st.markdown("Travel with respect. Travel with purpose. Discover India sustainably.")

    col1, col2 = st.columns([2, 1])  # Text wider, image narrower

    with col1:
        st.markdown("""
            Responsible tourism means **traveling in a way that minimizes negative impact** on the environment, 
            respects local cultures, and benefits local communities.

            Whether you're exploring the Himalayas, relaxing on a Goan beach, or wandering through Rajasthan's deserts — your choices matter.

            ---

            ✅ **Environmental Responsibility**  
            Travelers are encouraged to conserve natural resources, avoid pollution, and protect wildlife. This includes respecting biodiversity, staying on marked trails, and reducing your carbon footprint by choosing sustainable modes of transport.

            ✅ **Cultural Sensitivity**  
            Every region in India has its own traditions, languages, and social practices. Being respectful to local customs, dressing appropriately, and engaging with local heritage fosters deeper connections and avoids cultural imposition.

            ✅ **Community Empowerment**  
            Responsible tourism ensures that **local communities benefit directly** from tourism. This can include staying in family-run homestays, purchasing local handicrafts, and hiring local guides — creating jobs and preserving traditional livelihoods.

            ✅ **Sustainable Experiences**  
            Instead of high-impact luxury travel, responsible tourism promotes **low-impact, meaningful experiences** — such as participating in local festivals, volunteering for conservation, or learning indigenous crafts.

            ✅ **Leave No Trace**  
            It’s vital to leave tourist places as you found them — or better. Avoid littering, use reusable items, and don’t disturb natural habitats or cultural monuments.

            ---

            🌍 By choosing responsible tourism, you're not just a visitor — you're a contributor to a more sustainable, inclusive, and conscious way of exploring the world.
            """)

    with col2:
        banner = Image.open("images/incredible_india.jpg")
        st.image(banner, caption="Experience India Responsibly", use_container_width=True)

    # Full-width content continues after image height
    st.markdown("---")
    st.header("Principles of Responsible Travel")
    st.markdown("""
    - 🌱 **Respect Local Culture** – Dress modestly, ask before photographing people, and follow local customs.  
    - 🧼 **Minimize Waste** – Carry reusable bottles, bags, and avoid single-use plastics.  
    - 🚌 **Use Public Transport** – Choose local transport or shared travel options when possible.  
    - 🏡 **Support Local Businesses** – Stay in homestays, eat at local eateries, buy local handicrafts.  
    - 🐘 **Say No to Exploitation** – Avoid attractions that exploit animals or people.  
    - 🛤️ **Leave No Trace** – Take only memories, leave only footprints.  
    """)


    st.markdown("---")
    st.header("📍 State-wise Responsible Destinations")

    # --- Destination data ---
    destinations = [
        {
            "title": "Sikkim – India's First Organic State",
            "desc": (
                "Sikkim has set a global benchmark by becoming India's first fully organic state. "
                "Its commitment to banning chemical fertilizers and pesticides has helped preserve its rich biodiversity. "
                "The government actively promotes eco-friendly practices such as banning single-use plastics and supporting local homestays, "
                "ensuring that tourism benefits local communities. From terraced farms to ancient monasteries, visitors experience a blend of natural beauty and deep-rooted culture."
            ),
            "img": "images/sikkim.jpg",
            "link": "https://sikkimtourism.gov.in",
            "location": "https://www.google.com/maps/place/Sikkim"

        },
        {
            "title": "Mawlynnong, Meghalaya – Asia's Cleanest Village",
            "desc": (
                "Renowned as 'God’s own garden', Mawlynnong has earned its title as Asia’s cleanest village. "
                "This community-led model of cleanliness promotes waste segregation, composting, and plastic bans. "
                "Visitors are encouraged to follow eco-friendly practices while enjoying the village's stone pathways, bamboo skywalks, and hospitality in traditional homestays. "
                "Mawlynnong exemplifies how tourism and sustainable living can go hand in hand."
            ),
            "img": "images/mawlynnong.jpg",
            "link": "https://www.meghalayatourism.in",
            "location": "https://www.google.com/maps/place/Mawlynnong"

        },
        {
            "title": "Thenmala, Kerala – India’s First Eco-Tourism Hub",
            "desc": (
                "Nestled in the Western Ghats, Thenmala integrates adventure, nature, and culture with ecological awareness. "
                "It offers well-managed nature trails, forest treks, and tree-top huts while minimizing human impact on the environment. "
                "Cultural performances and local cuisine enhance the visitor experience, and eco-guides from nearby communities offer insight into conservation practices. "
                "Thenmala is a role model for responsible tourism in forest regions."
            ),
            "img": "images/thenmala.jpeg",
            "link": "https://www.thenmalaecotourism.com",
            "location": "https://www.google.com/maps/place/Thenmala"

        },
        {
            "title": "Khonoma, Nagaland – Conservation Village",
            "desc": (
                "Khonoma is a shining example of a community taking conservation into its own hands. "
                "Once reliant on hunting, this Angami tribal village has now banned hunting and created its own wildlife sanctuary. "
                "Tourists are welcomed into heritage homes and shown local customs and eco-friendly lifestyles. "
                "The village promotes cultural pride and biodiversity preservation while offering a serene experience."
            ),
            "img": "images/khonoma.jpg",
            "link": "https://tourism.nagaland.gov.in",
            "location": "https://www.google.com/maps/place/Khonoma"

        },
        {
            "title": "Majuli, Assam – World’s Largest River Island",
            "desc": (
                "Majuli is a cultural and ecological gem located in the Brahmaputra River. "
                "Its unique geography is complemented by the satras (monastic institutions) that preserve ancient Assamese arts, dance, and music. "
                "The island faces the threat of erosion, making responsible tourism crucial. Eco-friendly homestays and efforts to conserve wetland biodiversity are core to the experience. "
                "Travelers are encouraged to engage with local artisans and support traditional mask-making and pottery."
            ),
            "img": "images/majuli.jpg",
            "link": "https://tourism.assam.gov.in/portlets/majuli",
            "location": "https://www.google.com/maps/place/Majuli"

        },
        {
            "title": "Matheran, Maharashtra – India's Car-Free Hill Station",
            "desc": (
                "As India’s only automobile-free hill station, Matheran stands out for its clean air and peaceful ambiance. "
                "Visitors explore its scenic viewpoints via walking trails, horseback rides, or vintage toy trains. "
                "The absence of motor vehicles significantly reduces pollution and stress on the ecosystem. "
                "Sustainable practices such as rainwater harvesting and forest conservation make it a model for green getaways."
            ),
            "img": "images/matheran.jpeg",
            "link": "https://www.maharashtratourism.gov.in",
            "location": "https://www.google.com/maps/place/Matheran"

        },
        {
            "title": "Channapatna, Karnataka – Town of Toy Makers",
            "desc": (
                "Famous for its vibrant wooden toys, Channapatna supports an artisan economy rooted in centuries-old tradition. "
                "Tourism here directly uplifts local craftsmen and women who use sustainable materials and natural dyes. "
                "Workshops, guided tours, and artisan markets give travelers an immersive experience in ethical craft tourism. "
                "It’s a perfect blend of heritage preservation and community empowerment."
            ),
            "img": "images/channapatna.jpg",
            "link": "https://karnatakatourism.org/tour-item/channapatna",
            "location": "https://www.google.com/maps/place/Channapatna"
        },
        {
            "title": "Spiti Valley, Himachal Pradesh – High-Altitude Sustainability",
            "desc": (
                "Spiti Valley promotes sustainable tourism through eco-lodges, solar-powered homestays, and low-impact trekking. "
                "The local community, in partnership with NGOs, encourages waste reduction and cultural preservation. "
                "Visitors are immersed in high-altitude Himalayan life while contributing to environmental and cultural conservation efforts."
            ),
            "img": "images/spiti.jpeg",
            "link": "https://himachaltourism.gov.in",
            "location": "https://www.google.com/maps/place/Spiti+Valley"
        },
        {
            "title": "Araku Valley, Andhra Pradesh – Tribal Eco-Tourism",
            "desc": (
                "Nestled in the Eastern Ghats, Araku Valley is home to indigenous tribes and lush coffee plantations. "
                "Tourism initiatives focus on supporting tribal communities through guided cultural tours, organic coffee experiences, and eco-stays. "
                "It’s a peaceful retreat that celebrates tribal heritage and agro-ecological harmony."
            ),
            "img": "images/araku.jpg",
            "link": "https://tourism.ap.gov.in",
            "location": "https://www.google.com/maps/place/Araku+Valley"
        },
        {
            "title": "Ramnagar, Uttarakhand – Gateway to Wildlife Conservation",
            "desc": (
                "Adjacent to Jim Corbett National Park, Ramnagar is a responsible wildlife tourism base. "
                "Eco-resorts here promote conservation awareness, respect park rules, and collaborate with forest officials to ensure wildlife safety. "
                "Visitors learn about tiger conservation while enjoying guided nature trails and local culture."
            ),
            "img": "images/ramnagar.jpeg",
            "link": "https://uttarakhandtourism.gov.in",
            "location": "https://www.google.com/maps/place/Ramnagar"
        },
        {
            "title": "Auroville, Tamil Nadu – Experimental Sustainable Township",
            "desc": (
                "Auroville is an international township dedicated to sustainable living and human unity. "
                "It showcases renewable energy use, organic farming, waste management, and eco-architecture. "
                "Visitors engage in workshops and volunteering programs, offering a hands-on understanding of conscious living."
            ),
            "img": "images/auroville.jpeg",
            "link": "https://auroville.org",
            "location": "https://www.google.com/maps/place/Auroville"
        },
        {
            "title": "Bhuj, Gujarat – Post-Disaster Resilience and Craft Revival",
            "desc": (
                "After the 2001 earthquake, Bhuj emerged as a model of cultural resilience. "
                "The city now thrives on responsible tourism by supporting artisans of Bandhani, embroidery, and block printing. "
                "Craft-based homestays, craft villages like Bhujodi, and NGOs help visitors appreciate and contribute to heritage revival."
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


    m = folium.Map(location=[22.5937, 78.9629], zoom_start=5, tiles='cartodbpositron')

    for dest in destinations:
        if dest["title"] in lat_lon:
            lat, lon = lat_lon[dest["title"]]
            
            # Create an HTML popup with clickable link
            html = f'''
                <div>
                    <a href="{dest["location"]}" target="_blank" style="text-decoration:none; color:#007BFF;">
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
                icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(m)

    




    # --- Display the map in Streamlit ---
    st.subheader("🗺️ Explore Destinations on Interactive Map")
    # --- Center the map using columns ---
    left, center, right = st.columns([1, 3, 1])
    with center:
        st_folium(m, width=700, height=500)

    # --- Display cards in 2-column layout ---
    for i in range(0, len(destinations), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(destinations):
                dest = destinations[i + j]
                with cols[j]:
                    st.expander(f"📍 {dest['title']}")
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

    # --- Sustainable Destinations (Text only) ---
    st.header("Other Sustainable Destinations")
    st.markdown("""
    - 📍 **Spiti Valley** – Promotes community-based tourism and eco-stays  
    - 📍 **Coorg** – Offers eco-lodges and promotes agri-tourism  
    - 📍 **Kerala (Responsible Tourism Mission)** – Empowers local communities  
    - 📍 **Meghalaya** – Home to living root bridges and low-impact rural tourism  
    """)

    # --- Traveler Pledge ---
    st.header("Take the Responsible Traveler Pledge ✋")
    if st.button("I Pledge to Travel Responsibly"):
        st.success("Thank you! Your pledge supports a greener, more respectful India.")

    # --- Contact Section ---
    st.markdown("---")
    st.subheader("📬 Get Involved")
    st.markdown("Join the mission to promote sustainable tourism across India. Email us at [sustainable@tourismindia.org](mailto:sustainable@tourismindia.org)")

    # --- Footer ---
    st.markdown("---")
    st.caption("🇮🇳 Made with love for India's future | © 2025 Responsible Tourism India | Images used for educational purposes only.")
