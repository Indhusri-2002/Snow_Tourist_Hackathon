import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import textwrap
from utils.data_loader import load_datasets


def render():  
    # st.markdown(
    #     """
    #     <style>
    #     body, .main, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
    #         background-color: #D2D0A0 !important;
    #         color: black !important;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    dfs = load_datasets()
    total_jobs =  dfs['gdp_jobs'].loc[dfs['gdp_jobs']['YR'] == '2020', 'TOTAL'].values[0]
    latest_fee =  int(dfs['monthly_fee'].loc[dfs['monthly_fee']['YR'] == '2024', 'AUGUST'].values[0])/1000
    growth_rate = dfs['fee'].loc[dfs['fee']['YR'] == 2021,'FEE_GROWTH'].values[0]
    max_tourists = pd.to_numeric(dfs['tour_stat']['ITAS'], errors='coerce').max()
    # max_tourists = 17.91

    col1, col2, col3, col4 = st.columns(4)

    def kpi_card(title, value, subtitle="", delta=None):
        delta_html = ""
        if delta:
            delta_value = float(delta.replace('%', '').replace('+', ''))
            if delta_value < 0:
                delta_html = f"<p style='color:red; margin: 4px 0;'>▼ {abs(delta_value):.2f}%</p>"
            else:
                delta_html = f"<p style='color:green; margin: 4px 0;'>▲ {delta_value:.2f}%</p>"

        subtitle_html = f"<p style='color:gray; margin:4px 0;'>{subtitle}</p>" if subtitle else ""

        html = f"""
        <div style="border:1px solid #ccc; border-radius:10px; padding:15px; text-align:center;">
            <h4 style="margin-bottom:5px;">{title}</h4>
            <h2 style="margin:0;">{value}</h2>
            {delta_html}
            {subtitle_html}
        </div>
        """
        return textwrap.dedent(html)

    with col1:
        st.markdown(kpi_card("Total Tourism Jobs", f"{total_jobs} mil", "By 2020" , delta = "-1.97%"), unsafe_allow_html=True)

    with col2:
        st.markdown(kpi_card("Tourism FEE (in Rs)", f"{latest_fee}k", "By Aug 2024", delta = "-18.25%" ), unsafe_allow_html=True)

    with col3:
        st.markdown(kpi_card("YoY Growth - FEE", f"{growth_rate}", "By 2021", delta="103.3%"), unsafe_allow_html=True)

    with col4:
        st.markdown(kpi_card("Maximum Tourists", f"{max_tourists} mil", "In 2019" ,delta = "2.81%" ), unsafe_allow_html=True)

    
    st.markdown("---")
    df_fee = dfs['fee']
    st.markdown(
    "<h3 style='text-align: center; color: #F3F3E0;'>"
    "India’s Global Tourism Scorecard: How We Rank</h3>",
    unsafe_allow_html=True
    )
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

    st.markdown("---")
    st.markdown(
    "<h3 style='text-align: center; color: #F3F3E0;'>"
    "Who’s Visiting? A Look at FTAs, NRIs & ITAs</h3>",
    unsafe_allow_html=True
    )
    df_tour_stat = dfs['tour_stat']

    col1, col2 = st.columns(2)

    df_renamed = df_tour_stat.rename(columns={
    "FTAS": "Foreign Tourists",
    "NRIS": "NRIs",
    "ITAS": "Indian Tourists"
})
    with col1:
        fig_tourists = px.line(
            df_renamed,
            x="YR",
            y=["Foreign Tourists", "NRIs", "Indian Tourists"],
            markers=True,
            labels={
                "value": "Tourist Count in Millions",
                "variable": "Category",
                "YR": "Year"
            },
            title="Foreign Tourists (FTAs), NRIs, and Indian Tourists Over Years"
        )

        st.plotly_chart(fig_tourists, use_container_width=True)

    df_pct_renamed = df_tour_stat.rename(columns={
        "FTAS_PER_CHANGE": "FTAs % Change",
        "NRIS_PER_CHANGE": "NRIs % Change",
        "ITAS_PER_CHANGE": "ITAs % Change"
    })

    with col2:
        fig_pct = px.line(
            df_pct_renamed,
            x="YR",
            y=["FTAs % Change", "NRIs % Change", "ITAs % Change"],
            markers=True,
            labels={
                "value": "Percentage Change (%)",
                "variable": "Category",
                "YR": "Year"
            },
            title="Yearly % Change in FTAs, NRIs, and ITAs"
        )
        st.plotly_chart(fig_pct, use_container_width=True)



    df_jobs_gdp = dfs['gdp_jobs']
    df_jobs_gdp[["SHR_PER", "DIR_PER", "IND_PER", "GDP_SHR_PER", "TOTAL"]] = (
        df_jobs_gdp[["SHR_PER", "DIR_PER", "IND_PER", "GDP_SHR_PER", "TOTAL"]]
        .apply(pd.to_numeric, errors="coerce")
    )

    df_jobs_gdp["YR"] = df_jobs_gdp["YR"].astype(str)
    st.markdown("---")
    # st.subheader("Tourism Jobs and GDP Contribution Overview")
    st.markdown(
    "<h3 style='text-align: center; color: #F3F3E0; '>"
    "Tourism’s Payday: Jobs Created & GDP Boosted</h3>",
    unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    df_jobs_gdp_renamed = df_jobs_gdp.rename(columns={
        "SHR_PER": "Tourism Employment Share (%)",
        "DIR_PER": "Direct Employment by Tourism (%)",
        "IND_PER": "Indirect Employment by Tourism (%)"
    })

    with col1:
        fig1 = px.line(
            df_jobs_gdp_renamed,
            x="YR",
            y=[
                "Tourism Employment Share (%)",
                "Direct Employment by Tourism (%)",
                "Indirect Employment by Tourism (%)"
            ],
            labels={
                "value": "Percentage",
                "YR": "Year",
                "variable": "Employment Type"
            },
            markers=True,
            title="Share of Total, Direct & Indirect Tourism Jobs"
        )
        st.plotly_chart(fig1, use_container_width=True)


    with col2:
        fig2 = px.bar(
            df_jobs_gdp,
            x="YR",
            y="GDP_SHR_PER",
            labels={"GDP_SHR_PER": "GDP Share %", "YR": "Year"},
            title= "Tourism GDP Share Over the Years",
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        fig3 = px.area(
            df_jobs_gdp,
            x="YR",
            y="TOTAL",
            labels={"TOTAL": "Jobs (Millions)", "YR": "Year"},
            title = "Total Tourism Jobs (in Millions)"
        )
        st.plotly_chart(fig3, use_container_width=True)
    

    df_state_jobs = dfs['state_jobs']
    st.markdown("---")
    # st.subheader("Jobs by State (2015-16)")
    st.markdown(
    "<h3 style='text-align: center; color: #F3F3E0;'>"
    "State of Jobs: Who Hired the Most in Tourism?</h3>",
    unsafe_allow_html=True
    )
    col1, = st.columns(1)

    df_sorted = df_state_jobs.sort_values("JOB_COUNT")
    with col1:
        fig_state_jobs_heat = px.density_heatmap(
            df_sorted,
            y="STATE",
            x=["Jobs"] * len(df_sorted), 
            z="JOB_COUNT",
            color_continuous_scale="YlOrRd",
            labels={"z": "Tourism Jobs", "STATE": "State"},
            # title="Heatmap of Tourism-Related Jobs by State (2015-16)"
        )

        fig_state_jobs_heat.update_layout(xaxis_showticklabels=False)

        st.plotly_chart(fig_state_jobs_heat, use_container_width=True)

    
    st.markdown("---")
    # st.subheader("National Tourism Revenue Trends")
    st.markdown(
    "<h3 style='text-align: center; color: #F3F3E0;'>"
    "Money in Motion: Tracking Tourism Revenue</h3>",
    unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    df_fee_renamed = df_fee.rename(columns={
        "RECEIPTS_GROWTH": "Tourism Receipts Growth (%)",
        "FEE_GROWTH": "Foreign Exchange Earnings Growth (%)"
    })
    with col2:
        fig_growth = px.line(
            df_fee_renamed,
            x="YR",
            y=[
                "Tourism Receipts Growth (%)",
                "Foreign Exchange Earnings Growth (%)"
            ],
            markers=True,
            labels={
                "value": "Growth (%)",
                "YR": "Year",
                "variable": "Metric"
            },
            title="Yearly Growth in Receipts and Foreign Exchange Earnings"
        )
        st.plotly_chart(fig_growth, use_container_width=True)





    df_month = dfs['monthly_fee']

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
    df_melted["Fee"] = pd.to_numeric(df_melted["Fee"], errors="coerce") 
    df_melted = df_melted.sort_values(["YR", "Month"])


    with col1:
        fig_line = px.line(df_melted, x="Month", y="Fee", color="YR", markers=True,
                        labels={"Fee": "Fee Amount", "Month": "Month", "YR": "Year"},
                        title="Monthly Fee Trend by Year")
        st.plotly_chart(fig_line, use_container_width=True)



    df_scheme = dfs['scheme_amt']
    df_amt_ftas = dfs['amt_ftas']
    st.markdown("---")
    # st.subheader("Tourism Scheme Funding Overview")
    st.markdown(
    "<h3 style='text-align: center; color: #F3F3E0; '>"
    "Fueling Tourism: Where the Government Invests</h3>",
    unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
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
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=df_amt_ftas["YR"], y=df_amt_ftas["AMT_SANC"], name="Amount Sanctioned (Cr)",
            marker_color="royalblue", yaxis="y1"
        ))

        fig.add_trace(go.Scatter(
            x=df_amt_ftas["YR"], y=df_amt_ftas["FTAS"], name="Foreign Tourist Arrivals (Mil)",
            mode="lines+markers", marker_color="orange", yaxis="y2"
        ))

        fig.update_layout(
            xaxis=dict(title="Year"),
            yaxis=dict(title="Amount Sanctioned (Cr)", side="left"),
            yaxis2=dict(title="FTAs (Mil)", overlaying="y", side="right"),
            legend=dict(x=0.01, y=0.99),
            height=500,
            title = "Amount Sanctioned vs Foreign Tourist Arrivals"
        )

        st.plotly_chart(fig)