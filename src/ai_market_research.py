import sqlite3, pandas as pd

class AIMarketResearchAgent:
    def __init__(self, db_path="data/energy_market.db"):
        self.db_path = db_path

    def generate_executive_brief(self, region="Asia-Pacific"):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM energy_market_metrics WHERE region = ? ORDER BY report_date DESC LIMIT 30", conn, params=(region,))
        conn.close()
        latest = df.iloc[0]
        return f"AI MARKET BRIEF [{region}] | Date: {latest['report_date']} | Brent: ${latest['brent_crude_usd']} | Demand: {latest['electricity_demand_gwh']} GWh | Renewables: {latest['renewable_share_pct']}%"
