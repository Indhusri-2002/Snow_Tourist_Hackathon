import streamlit as st
import pandas as pd
import plotly.express as px
from services.snowflake_connector import get_snowflake_connection

@st.cache_data(ttl=600)
def load_all_data():
    #avi
    conn = get_snowflake_connection()

    try:
        df_fee = pd.read_sql("SELECT * FROM CURATE.FCT_FEE_INDIA_RNK", conn)
        # df_gdp = pd.read_sql("SELECT * FROM CURATE.FCT_GDP_JOBS_MIL", conn)
        # df_jobs_cat = pd.read_sql("SELECT * FROM CURATE.FCT_JOBS_CAT_MIL", conn)
        df_state_jobs = pd.read_sql("SELECT * FROM STAGE.STG_STATE_JOBS_15_16_LAKH", conn)
        df_scheme_amt = pd.read_sql("SELECT * FROM STAGE.STG_SCHEME_AMT", conn)
        df_tour_stat = pd.read_sql("SELECT * FROM STAGE.STG_TOUR_STAT", conn)
        df_monthly_fee = pd.read_sql("SELECT * FROM STAGE.STG_IND_FEE", conn)
        df_gdp_jobs = pd.read_sql("SELECT * FROM CURATE.FCT_JOBS_GDP_CAT_MIL", conn)

    finally:
        conn.close()

    return {
        "fee": df_fee,
        # "gdp": df_gdp,
        # "jobs_cat": df_jobs_cat,
        "gdp_jobs" : df_gdp_jobs,
        "state_jobs": df_state_jobs,
        "scheme_amt": df_scheme_amt,
        "tour_stat": df_tour_stat,
        "monthly_fee": df_monthly_fee,
    }


def render():
    dfs = load_all_data()
    df_fee = dfs['fee']

    st.subheader("India's Global Tourism Share and Rank")
    col3, col4 = st.columns(2)

    with col3:
        fig_share = px.line(df_fee, x="YR", y="PER_SHR_IND", markers=True,
                            labels={"YR": "Year", "PER_SHR_IND": "India's % Share"},
                            title="India's Share in Global Tourism")
        st.plotly_chart(fig_share, use_container_width=True)

    with col4:
        fig_rank = px.line(df_fee, x="YR", y="IND_RANK", markers=True,
                        labels={"YR": "Year", "IND_RANK": "India's Global Rank"},
                        title="India's Global Tourism Rank Over Time")
        fig_rank.update_traces(line=dict(color="firebrick", width=2), marker=dict(size=8))
        fig_rank.update_yaxes(title="Rank (Lower is Better)")
        st.plotly_chart(fig_rank, use_container_width=True)

    # --- Visualizations ---
    st.header("Tourist Categories Overview (FTAs, NRIs, ITAs)")
    df_tour_stat = dfs['tour_stat']

    col1, col2 = st.columns(2)

    with col1:
        fig_tourists = px.line(
            df_tour_stat,
            x="YR",
            y=["FTAS", "NRIS", "ITAS"],
            markers=True,
            labels={"value": "Tourist Count in Millions", "variable": "Category", "YR": "Year"},
            title="Foreign Tourists (FTAs), NRIs, and ITAs Over Years"
        )
        st.plotly_chart(fig_tourists, use_container_width=True)

    with col2:
        fig_pct = px.line(
            df_tour_stat,
            x="YR",
            y=["FTAS_PER_CHANGE", "NRIS_PER_CHANGE", "ITAS_PER_CHANGE"],
            markers=True,
            labels={"value": "Percentage Change (%)", "variable": "Category", "YR": "Year"},
            title="Yearly % Change in FTAs, NRIs, and ITAs"
        )
        st.plotly_chart(fig_pct, use_container_width=True)



# Ensure numeric columns are converted properly
    df_jobs_gdp = dfs['gdp_jobs']
    df_jobs_gdp[["SHR_PER", "DIR_PER", "IND_PER", "GDP_SHR_PER", "TOTAL"]] = (
        df_jobs_gdp[["SHR_PER", "DIR_PER", "IND_PER", "GDP_SHR_PER", "TOTAL"]]
        .apply(pd.to_numeric, errors="coerce")
    )

    df_jobs_gdp["YR"] = df_jobs_gdp["YR"].astype(str)

    st.subheader("Tourism Jobs and GDP Contribution Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        # st.markdown("#### Share of Total, Direct & Indirect Tourism Jobs")
        fig1 = px.line(
            df_jobs_gdp,
            x="YR",
            y=["SHR_PER", "DIR_PER", "IND_PER"],
            labels={"value": "Percentage", "YR": "Year", "variable": "Type"},
            markers=True,
            title = "Share of Total, Direct & Indirect Tourism Jobs"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # st.markdown("#### Tourism GDP Share Over the Years")
        fig2 = px.bar(
            df_jobs_gdp,
            x="YR",
            y="GDP_SHR_PER",
            labels={"GDP_SHR_PER": "GDP Share %", "YR": "Year"},
            title= "Tourism GDP Share Over the Years",
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        # st.markdown("#### Total Tourism Jobs (in Millions)")
        fig3 = px.area(
            df_jobs_gdp,
            x="YR",
            y="TOTAL",
            labels={"TOTAL": "Jobs (Millions)", "YR": "Year"},
            title = "Total Tourism Jobs (in Millions)"
        )
        st.plotly_chart(fig3, use_container_width=True)
    

    df_state_jobs = dfs['state_jobs']
# --- Visualizations ---
    st.header("Jobs by State (2015-16)")
    col1, = st.columns(1)

    # with col1:
    #     # st.subheader("Jobs by State (Horizontal Bar Chart)")
    #     fig_state_jobs_h = px.bar(
    #         df_state_jobs.sort_values("JOB_COUNT", ascending=True),
    #         x="JOB_COUNT",
    #         y="STATE",
    #         orientation='h',
    #         labels={"STATE": "State", "JOB_COUNT": "Number of Jobs"},
    #         title="Tourism-Related Jobs by State (2015-16)",
    #         height=600,
    #     )
    #     st.plotly_chart(fig_state_jobs_h, use_container_width=True)

    with col1:
        # st.subheader("Jobs Distribution by State (Donut Chart)")
        fig_state_jobs_donut = px.pie(
            df_state_jobs,
            names='STATE',
            values='JOB_COUNT',
            hole=0.4,
            title="Tourism-Related Jobs by State (2015-16)"
        )
        st.plotly_chart(fig_state_jobs_donut, use_container_width=True)

    

    st.header("National Tourism Revenue Trends")

    col1, col2 = st.columns(2)

    # with col1:
    #     # st.subheader("Total Receipts Over Years")
    #     fig = px.line(df_fee, x="YR", y="RECEIPTS", markers=True,
    #                 labels={"YR": "Year", "RECEIPTS": "Receipts (in Dol)"},
    #                 title="Tourism Receipts Over Years")
    #     st.plotly_chart(fig, use_container_width=True)

    with col2:
        # st.subheader("Receipts Growth & Fee Growth (%)")
        fig_growth = px.line(df_fee, x="YR", y=["RECEIPTS_GROWTH", "FEE_GROWTH"],
                            markers=True,
                            labels={"value": "Growth (%)", "YR": "Year", "variable": "Metric"},
                            title="Yearly Growth in Receipts and Fee")
        st.plotly_chart(fig_growth, use_container_width=True)




    df_month = dfs['monthly_fee']

    # Melt the data to long format for month-wise plotting
    df_melted = df_month.melt(id_vars="YR", var_name="Month", value_name="Fee")
    month_order = ['JANUARY',
                    'FEBRUARY',
                    'MARCH',
                    'APRIL',
                    'MAY',
                    'JUNE',
                    'JULY',
                    'AUGUST',
                    'SEPTEMBER',
                    'OCTOBER',
                    'NOVEMBER',
                    'DECEMBER'
                    ]
    df_melted["Month"] = pd.Categorical(df_melted["Month"], categories=month_order, ordered=True)
    df_melted["Fee"] = pd.to_numeric(df_melted["Fee"], errors="coerce")  # Convert Fee to numeric
    df_melted = df_melted.sort_values(["YR", "Month"])

    # col1, col2 = st.columns(2)

    with col1:
        fig_line = px.line(df_melted, x="Month", y="Fee", color="YR", markers=True,
                        labels={"Fee": "Fee Amount", "Month": "Month", "YR": "Year"},
                        title="Monthly Fee Trend by Year")
        st.plotly_chart(fig_line, use_container_width=True)

    # with col2:
    #     avg_fee_by_month = df_melted.groupby("Month")["Fee"].mean().reset_index()
    #     fig_bar = px.bar(avg_fee_by_month, x="Month", y="Fee",
    #                     labels={"Fee": "Avg Fee", "Month": "Month"},
    #                     title="Average Monthly Fee (Across All Years)")
    #     st.plotly_chart(fig_bar, use_container_width=True)



    df_scheme = dfs['scheme_amt']

    st.header("Tourism Scheme Funding Overview")

    col1, col2 = st.columns(2)

    with col1:
        # st.subheader("Yearly Amount Sanctioned (Total)")
        # df_sanc_yearly = df_scheme.groupby("YR")["AMT_SANC"].sum().reset_index()
        df_scheme["AMT_SANC"] = pd.to_numeric(df_scheme["AMT_SANC"], errors="coerce")

        df_sanc_yearly = (
            df_scheme.groupby("YR")["AMT_SANC"]
            .sum()
            .reset_index()
        )

        fig_sanc_yearly = px.line(df_sanc_yearly, x="YR", y="AMT_SANC",
                                markers=True,
                                labels={"AMT_SANC": "Amount Sanctioned (₹ Cr)", "YR": "Year"},
                                title="Trend of Amount Sanctioned Over the Years")
        st.plotly_chart(fig_sanc_yearly, use_container_width=True)


    with col2:
        # st.subheader("Top Circuits by Amount Sanctioned")
        df_top_circuits = df_scheme.groupby("CIRCUIT")["AMT_SANC"].sum().reset_index()
        df_top_circuits = df_top_circuits.sort_values("AMT_SANC", ascending=False).head(10)

        fig_top_circuits = px.bar(df_top_circuits, x="AMT_SANC", y="CIRCUIT", orientation="h",
                                labels={"AMT_SANC": "Amount Sanctioned (₹ Cr)", "CIRCUIT": "Circuit"},
                                title="Top 10 Circuits by Sanctioned Amount")
        st.plotly_chart(fig_top_circuits, use_container_width=True)




