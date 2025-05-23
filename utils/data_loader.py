import streamlit as st
import pandas as pd
from services.snowflake_connector import get_snowflake_connection

@st.cache_data(ttl=600)
def load_datasets():
    conn = get_snowflake_connection()
    try:
        df_fee = pd.read_sql("SELECT * FROM CURATE.FCT_FEE_INDIA_RNK", conn)
        df_state_jobs = pd.read_sql("SELECT * FROM STAGE.STG_STATE_JOBS_15_16_LAKH", conn)
        df_scheme_amt = pd.read_sql("SELECT * FROM STAGE.STG_SCHEME_AMT", conn)
        df_tour_stat = pd.read_sql("SELECT * FROM STAGE.STG_TOUR_STAT", conn)
        df_monthly_fee = pd.read_sql("SELECT * FROM STAGE.STG_IND_FEE", conn)
        df_gdp_jobs = pd.read_sql("SELECT * FROM CURATE.FCT_JOBS_GDP_CAT_MIL", conn)
        df_amt_ftas = pd.read_sql("SELECT * FROM CURATE.FCT_AMT_FTAS", conn)
        df_artforms = pd.read_sql("SELECT * FROM STAGE.STG_ARTFORMS_OF_INDIA", conn)
        df_experiences = pd.read_sql("SELECT * FROM STAGE.STG_CULTURAL_EXPERIENCES", conn)
        df_places_to_visit = pd.read_sql("SELECT * FROM STAGE.STG_PLACES_TO_VISIT", conn)
        df_untouched_places = pd.read_sql("SELECT * FROM STAGE.STG_UNTOUCHED_PLACES_LAT_LON", conn)
    finally:
        conn.close()

    return {
        "fee": df_fee,
        "gdp_jobs": df_gdp_jobs,
        "state_jobs": df_state_jobs,
        "scheme_amt": df_scheme_amt,
        "tour_stat": df_tour_stat,
        "monthly_fee": df_monthly_fee,
        "amt_ftas":df_amt_ftas,
        "art_forms":df_artforms,
        "experiences":df_experiences,
        "places_to_visit": df_places_to_visit,
        "untouched_places": df_untouched_places
    }
