# 🇮🇳 Soul of India – A Data-Driven Responsible Tourism Guide

**Soul of India** is a Streamlit-powered platform developed as part of the Snowflake Tourism Hackathon.  
It celebrates the vibrant culture, heritage, and sustainable tourism practices of India through interactive visualizations, maps, and curated insights.

🌐 **Live Site**: [soul-of-india.streamlit.app](https://soul-of-india.streamlit.app/)

---

## 🧩 Problem Statement

Tourism is a vital sector for India's economy but faces challenges such as over-tourism, environmental degradation, and loss of cultural heritage. There is a pressing need for tools that promote responsible tourism by raising awareness, supporting local communities, and preserving India’s rich cultural diversity.

The challenge requires innovative data-driven solutions to:

- Showcase India’s diverse art, culture, and heritage.  
- Provide insightful tourism analytics and economic impact data.  
- Encourage sustainable and responsible travel practices.  
- Highlight lesser-known, untouched destinations for balanced tourism growth.

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