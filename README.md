# 🇮🇳 Soul of India – A Data-Driven Responsible Tourism Guide

**Soul of India** is a Streamlit-powered platform developed as part of the Snowflake Tourism Hackathon.  
It celebrates the vibrant culture, heritage, and sustainable tourism practices of India through interactive visualizations, maps, and curated insights.

🌐 **Live Site**: [soul-of-india.streamlit.app](https://soul-of-india.streamlit.app/)

---

## 🧩 Problem Statement

Design, develop, and produce a solution on Streamlit that showcases traditional art forms, uncovers cultural experiences offered across the country, and promotes responsible tourism.

**Context:**

India's art and culture space is incredibly diverse and rich, encompassing a wide array of traditions and beliefs, influenced by both ancient and modern times, as well as regional, religious and cultural elements. Dive into the heart of India's artistic and cultural heritage with a story that can enrich both the traveller's journey and the preservation of our cultural treasures—the data-first way!

**Resources:**

1. Explore government contributions to improve art, culture and heritage in India, and discover how it is linked with tourism by exploring data on https://www.data.gov.in.

2. Find out seasonalities and trends in tourism to cultural hotspots. Identify areas that are relatively untouched and why they are so.

3. Create a story covering all these aspects through Snowflake and Streamlit.
---


## 💡 Our Solution: Soul of India

Soul of India is a Streamlit-based web application designed as a comprehensive platform to promote responsible tourism in India through rich cultural exploration and data-driven insights.

### 🧭 Key Features

- **Explore India**: Dive into the diverse art forms, cultural experiences, and UNESCO World Heritage sites across India.  
- **Tourism Insights**: Visualize the state of tourism economy, job statistics, and foreign exchange earnings with interactive charts and data.  
- **Responsible Tourism**: Learn mindful travel practices and discover eco-friendly, community-driven destinations state-wise.  
- **Untouched Places**: Find hidden gems and pristine places off the beaten path, encouraging sustainable tourism spread.  

---

## 🛠️ Technology Stack & Tools

- Python, Streamlit (for frontend and backend)  
- Snowflake (for data storage and querying)  
- Pandas, Plotly, Folium (for data processing and visualizations)  
- streamlit-option-menu, streamlit-folium (UI enhancements)  

---

## 🧾 Requirements

Install these Python dependencies before running the app:

```txt
streamlit
snowflake-connector-python
pandas
plotly>=5.0.0
folium
streamlit-folium
```

---

## ❄️ Snowflake Configuration

To connect the app to Snowflake, create a `.streamlit/secrets.toml` file in your project root with the following keys:

```toml
# .streamlit/secrets.toml

account = "your_snowflake_account"
user = "your_snowflake_username"
password = "your_snowflake_password"
role = "your_role_name"
warehouse = "your_warehouse_name"
database = "your_database_name"
schema = "your_schema_name"


## 🚀 How to Run / Setup

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Indhusri-2002/Snow_Tourist_Hackathon.git
```
```bash
cd Snow_Tourist_Hackathon
```

### 2. (Optional) Create a Virtual Environment
Creating a virtual environment helps keep dependencies isolated.

#### For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run main.py
```