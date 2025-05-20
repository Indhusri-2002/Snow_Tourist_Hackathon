import streamlit as st
import pandas as pd
from  services.snowflake_connector import get_snowflake_connection

def render():
    st.title("📈 Analytics")
    conn = get_snowflake_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM STAGE.STG_JOBS_CAT")
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
    finally:
        cur.close()
