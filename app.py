import sqlite3, pandas as pd, plotly.express as px, streamlit as st
from src.ai_market_research import AIMarketResearchAgent

st.set_page_config(page_title="EnergyPulse AI", layout="wide")
st.title("EnergyPulse AI: Global Energy & Commodity Market Intelligence")
conn = sqlite3.connect("data/energy_market.db")
df = pd.read_sql_query("SELECT * FROM energy_market_metrics", conn)
conn.close()
region = st.sidebar.selectbox("Select Region", df["region"].unique())
reg_df = df[df["region"] == region].sort_values("report_date")
st.plotly_chart(px.line(reg_df, x="report_date", y="electricity_demand_gwh", title=f"{region} Electricity Demand (GWh)"), use_container_width=True)
st.text(AIMarketResearchAgent().generate_executive_brief(region))
