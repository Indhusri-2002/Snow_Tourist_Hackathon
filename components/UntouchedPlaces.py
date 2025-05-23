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

lat_lon = {
    "Gurez Valley": [34.6333, 74.8333, "https://www.google.com/maps/place/Gurez+Valley,+Forest+Block/@34.6477025,74.6103283,11z/data=!3m1!4b1!4m6!3m5!1s0x38e1432a23b9b275:0xccbcb398e000ad16!8m2!3d34.6494398!4d74.736633!16s%2Fm%2F05h30cm?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Phugtal Gompa": [33.0400, 77.3200, "https://www.google.com/maps/place/Phukthar+Gompa/@33.268189,77.1771803,17z/data=!3m1!4b1!4m6!3m5!1s0x3902f8637a343233:0xe595bcedd1aa3ed8!8m2!3d33.268189!4d77.1797552!16s%2Fm%2F05p72nv?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Chopta": [30.3464, 79.0484, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=Chopta&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUba76WL62NDKV-tuv6_wPYBC9v7ob7zIjaDzKC7u3qUzfBSmKk6Pff1pqd8YfYoBWgxShjObchCB7wdFhyLTfFLfus5TliiWCeq3VaHGAI0oni_PBrP80yVEAM1u_bASNBcRCTP1SY7iG7IDZXPNOFx8IcWjig&entry=mc&ved=1t:200715&ictx=111"],
    "Kanatal": [30.4153, 78.3211, "https://www.google.com/maps/place/Kanatal,+Kaudia+Range,+Uttarakhand+249130/@30.4137777,78.3246658,14z/data=!3m1!4b1!4m6!3m5!1s0x3908e1a9660030ed:0x5730466a139782a4!8m2!3d30.4137449!4d78.3458198!16s%2Fm%2F0g5qhv7?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Damro": [28.1238, 95.1634, "https://www.google.com/maps/place/Rane+Monying/@28.4221717,95.0658507,11.81z/data=!4m9!1m2!2m1!1sdamro+arunachal+pradesh!3m5!1s0x373fe5dd05b66d3d:0x96144ab98bd0736!8m2!3d28.4303241!4d95.2517723!16s%2Fg%2F11t_s4l68h?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Mawlynnong": [25.1833, 91.9667, "https://www.google.com/maps/place/Mawlynnong,+Meghalaya+793109/@25.2019662,91.9067029,15z/data=!3m1!4b1!4m6!3m5!1s0x37505c6a863d83f1:0x3d3d8ad73774eec1!8m2!3d25.2017637!4d91.9160305!16s%2Fm%2F0807rv9?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Sandakphu": [27.1036, 87.9983, "https://www.google.com/maps/place/Sandakphu/@27.059998,87.9794004,14z/data=!3m1!4b1!4m6!3m5!1s0x39e5da1c85bf30d7:0x7c65ec6d4307277!8m2!3d27.06!4d88!16zL20vMGd0dzky?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Kila Raipur": [30.7624, 75.8229, "https://www.google.com/maps/place/Kila+Raipur,+Punjab/@30.7615388,75.8126485,15z/data=!3m1!4b1!4m6!3m5!1s0x3910795b7326f365:0x11f691181cae4679!8m2!3d30.762428!4d75.8228899!16zL20vMDVzNV9m?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Jawai": [25.0906, 73.1494, "https://www.google.com/maps/place/Jawai+River/@25.0663382,72.1561715,9z/data=!3m1!4b1!4m6!3m5!1s0x3942ee426c2306d3:0xe824d42bb51acc9c!8m2!3d25.1560909!4d72.9404131!16s%2Fm%2F063zyxq?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Mohammadpur Umri": [25.4400, 81.7400, "https://www.google.com/maps/place/Mohammadpur+Umri,+Bamrauli,+Prayagraj,+Uttar+Pradesh+211012/@25.4392116,81.7358667,15z/data=!3m1!4b1!4m6!3m5!1s0x399accce2bef5ea7:0x976ee7401d9fe71e!8m2!3d25.4407555!4d81.7417812!16s%2Fm%2F0125wl6g?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Amadubi": [22.6500, 86.3500, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=Amadubi&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUba76WL62NDKV-tuv6_wPYBC9v7ob7zIjaDzKC7u3qUzfD7e7YM11gPmU080OmUCW2ra6dnp670CRAaKtkLzGbsTDSqnsqGdRqpRgn7m8J8sRSSZQGr1gsZNygXo3gegFkXRGx97PLV94iHXkSHBuVAPRbU0rg&entry=mc&ved=1t:200715&ictx=111"],
    "Mainpat": [22.7800, 83.3500, "https://www.google.com/maps/place/Mainpat,+Chhattisgarh+497111/@22.8199076,83.2622335,14z/data=!3m1!4b1!4m6!3m5!1s0x3989eb48d0ef9ef7:0xd68a3e2cf317c442!8m2!3d22.8199093!4d83.2828331!16s%2Fm%2F010fbzyn?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Lepakshi": [13.8100, 77.6000, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=Lepakshi&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUba76WL62NDKV-tuv6_wPYBC9v7ob7zIjaDzKC7u3qUzfD7e7YM11gPmU080OmUCW2ra6dnp670CRAaKtkLzGbsTDSqnsqGdRqpRgn7m8J8sRSSZQGr1gsZNygXo3gegFkXRGx97PLV94iHXkSHBuVAPRbU0rg&entry=mc&ved=1t:200715&ictx=111"],
    "Parule and Bhogwe": [15.9570, 73.5040, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=Parule+and+Bhogwe&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUba76WL62NDKV-tuv6_wPYBCQ_izzuyJPycJyJkI2VDlEb7_-rGWzmKh9xzGT6yfPJ4wTb5oB8eDIq-AmU2sM_mdc8GEGxMLqp7owfobGkGd_h3GdOnsxC0OP3YFIsNm5eB3YaK3wXpn6LxGI_5VW7cXaAVdXA&entry=mc&ved=1t:200715&ictx=111"],
    "Velas": [17.9588, 73.0361, "https://www.google.com/maps/place/Velas+Turtle+Festival/@17.9623181,73.0206301,15.66z/data=!4m15!1m8!3m7!1s0x3be9b42c4b6751bb:0xf9fd95a5b7147a60!2sVelas,+Maharashtra+415208!3b1!8m2!3d17.9588484!4d73.0361003!16s%2Fm%2F0h1cgvs!3m5!1s0x3be9b5550c206f4d:0x2629da3adc9ea145!8m2!3d17.9573259!4d73.0302168!16s%2Fg%2F11fjqk1z2p?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Halebidu": [13.2170, 75.9911, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=Halebidu&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUba76WL62NDKV-tuv6_wPYBC9v7ob7zIjaDzKC7u3qUzfD7e7YM11gPmU080OmUCW2ra6dnp670CRAaKtkLzGbsTDSqnsqGdRqpRgn7m8J8sRSSZQGr1gsZNygXo3gegFkXRGx97PLV94iHXkSHBuVAPRbU0rg&entry=mc&ved=1t:200715&ictx=111"],
    "Daroji Sloth Bear Sanctuary": [15.2353, 76.4742, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=daroji+sloth+bear+sanctuary&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUbalBeyXa8ssyRd_VUj5FQB2orc_91wYCtVawaLNWtsSduS5mUJudDN6Xwi5REd7v6dTe2rYQTEJ17YcJwB_BAI750yute0TwlgDoAUC93mpFZeUKpZg8izpqDEXIThPS2KJ7P2YKcU4nCuj0SyWipL9BUi8rQ&entry=mc&ved=1t:200715&ictx=111"],
    "Moodbidri": [13.0667, 74.9997, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&sxsrf=AE3TifOI05TaWE9jEESBQCC1ONkl_kwEPw:1747993461280&q=moodbidri&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZMLQ4RPdPjLPmOakFCN7X8EE7njRrb2FMGWExx-5ARS2dDjUqH8P7GJI3gXZTNa1egWDXHZA7uol1xYheZpR0TkaHevjzQPA27imLYTACFW1AS9_XARWhCazV31CgahQR4DA0KzL29oe2qokyYxvHjdHCMvkZXVXM3LddtFancVUzA74GKjbYff9zm0eS5B9Dx62YJg&biw=1710&bih=908&dpr=2&um=1&ie=UTF-8&ved=1t:200715&ictx=111"],
    "Chembra Lake": [11.5524, 76.0720, "https://www.google.com/maps/place/Chembra+Peak+Heart+Lake/@11.5472644,76.0617558,14z/data=!3m1!4b1!4m6!3m5!1s0x3ba66d55a94df537:0x781566df4847044b!8m2!3d11.5472654!4d76.0823554!16s%2Fg%2F1ptx4cvxv?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Urakam": [10.4530, 76.2103, "https://www.google.com/maps/place/Urakathamma+Thiruvadi+Temple/@10.4264493,76.2042096,15z/data=!4m15!1m8!3m7!1s0x3ba7f1227388a45b:0xcf9f215db08d0521!2sUrakam,+Thrissur,+Kerala+680562!3b1!8m2!3d10.4273905!4d76.2160448!16s%2Fg%2F12qgxs2qd!3m5!1s0x3ba7f122ae6cdd4b:0x9b4dd1d3b56747da!8m2!3d10.4294302!4d76.213569!16s%2Fm%2F025vt8n?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Ziro": [27.6000, 93.8333, "https://www.google.com/maps/place/Ziro+791120/@27.5465514,93.7975543,14z/data=!3m1!4b1!4m6!3m5!1s0x3741612864517cd3:0xb9e78639773cc4ea!8m2!3d27.544912!4d93.8196686!16zL20vMDJfZzNw?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Mawsynram": [25.2986, 91.5822, "https://www.google.com/maps/place/M%C4%81wsynr%C4%81m,+Meghalaya+793113/@25.2994013,91.560319,14z/data=!3m1!4b1!4m6!3m5!1s0x37509495e5bc131b:0x9db24bbe6c10df77!8m2!3d25.2973371!4d91.5826509!16zL20vMDQ4enJu?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Majuli": [26.9545, 94.1450, "https://www.google.com/maps/place/Majuli/@27.007104,93.86502,10z/data=!3m1!4b1!4m6!3m5!1s0x3746c41068c5707f:0x3dd7532bf70e8c60!8m2!3d27.0016172!4d94.2242981!16zL20vMDNsY3B4?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Tawang": [27.5867, 91.8650, "https://www.google.com/maps/place/Tawang+790104/@27.5885206,91.8320747,14.91z/data=!4m6!3m5!1s0x375cf4f8474f47b7:0x6448080fa5e6771c!8m2!3d27.5860574!4d91.8594062!16s%2Fg%2F1q6j34wfl?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Champaner": [22.4900, 73.5300, "https://www.google.com/maps/place/Champaner,+Gujarat+389360/@22.4844949,73.5220313,15z/data=!3m1!4b1!4m6!3m5!1s0x39607e5d68c3e075:0x32a544c438221ba5!8m2!3d22.4844703!4d73.5314366!16zL20vMDgwbGxi?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Kurnool": [15.8281, 78.0373, "https://www.google.com/maps?sca_esv=acdf4b34b1441e50&output=search&q=kurnool&source=lnms&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZMLQ4RPdPjLPmOakFCN7X8EE7njRrb2FMGWExx-5ARS2ePkf3FsHWrPuNuW8Cq2QqtEi-S3UAAE4rwi1cMD7l2vGmSNd51yxY3Q7AazeU7576xKI3BH4cHek3cCbYk3nTYGQX-pj9YFmit5y19U69rT6QH5B28Zpf_3NU5EqxKI0NgcxPd3SLZlPfghS2zkmJwgnYNg&entry=mc&ved=1t:200715&ictx=111"],
    "Hemis": [33.8833, 77.7000, "https://www.google.com/maps/place/Hemis+194201/@33.9139916,77.6987887,15z/data=!3m1!4b1!4m6!3m5!1s0x38fdf7b7c14b0e3d:0x8c32668a6bea2e2a!8m2!3d33.9136846!4d77.710153!16zL20vMGdqbjZi?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Patan": [23.8500, 72.1167, "https://www.google.com/maps/place/Patan,+Gujarat/@23.8481782,72.0811261,13z/data=!3m1!4b1!4m6!3m5!1s0x395c87925f115695:0x6f1db1097c4ff9ce!8m2!3d23.8500156!4d72.1210274!16zL20vMDRyMjR4?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Mandu": [22.3667, 75.3833, "https://www.google.com/maps/place/Mandav,+Madhya+Pradesh/@22.3347761,75.3645791,13z/data=!3m1!4b1!4m6!3m5!1s0x396241df36b705c1:0xb18ad666203d2d29!8m2!3d22.3339828!4d75.4003026!16zL20vMDNwNnY4?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
    "Lunglei": [22.8800, 92.7300, "https://www.google.com/maps/place/Lunglei,+Mizoram/@22.9004205,92.6807967,12z/data=!3m1!4b1!4m6!3m5!1s0x374d40ea4576cfd5:0x522da0079b07c840!8m2!3d22.8889908!4d92.7455429!16zL20vMDhiMnNx?entry=ttu&g_ep=EgoyMDI1MDUxNS4xIKXMDSoASAFQAw%3D%3D"],
}


def untouched_places():
    st.title("Untouched Places in India")

    dfs = load_datasets()
    df_untouched = dfs['untouched']

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
        if place in lat_lon:
            lat, lon, link = lat_lon[place]
            popup_html = f"<b>{place}</b><br><a href='{link}' target='_blank'>Open in Google Maps</a>"
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=place,
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)

    st.subheader("📍 Map View")

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
            link = lat_lon.get(place, [None, None, "#"])[2]

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

        st.subheader("🗺️ Explore some untouched places")
        card_html = ""

        for _, row in df_filtered.iterrows():
            place = row["PLACE"]
            state = row["STATE_UT"]
            reason = row["REASON"]
            season = row["BEST_SEASON"]
            image_path = f"images/untouched_places/{place.lower().replace(' ', '_')}.jpeg"
            link = lat_lon.get(place, [None, None, "#"])[2]

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
