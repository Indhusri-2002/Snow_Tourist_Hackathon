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
        df_untouched = pd.read_sql("SELECT * FROM STAGE.STG_UNTOUCHED_PLACES", conn)
        df_amt_ftas = pd.read_sql("SELECT * FROM CURATE.FCT_AMT_FTAS", conn)

    finally:
        conn.close()

    return {
        "fee": df_fee,
        "gdp_jobs": df_gdp_jobs,
        "state_jobs": df_state_jobs,
        "scheme_amt": df_scheme_amt,
        "tour_stat": df_tour_stat,
        "monthly_fee": df_monthly_fee,
        "untouched": df_untouched,
        "amt_ftas":df_amt_ftas,
    }
