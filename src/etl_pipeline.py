import sqlite3, logging
from datetime import datetime, timedelta
import numpy as np, pandas as pd
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class EnergyRecordSchema(BaseModel):
    report_date: str
    region: str
    brent_crude_usd: float = Field(gt=0, lt=300)
    henry_hub_gas_usd: float = Field(gt=0, lt=50)
    electricity_demand_gwh: float = Field(gt=0)
    renewable_share_pct: float = Field(ge=0, le=100)
    carbon_intensity_gco2: float = Field(ge=0)
    ai_sentiment_score: float = Field(ge=-1.0, le=1.0)

class EnergyETLPipeline:
    def __init__(self, db_path="data/energy_market.db"):
        self.db_path = db_path

    def run_pipeline(self, days=365):
        np.random.seed(42)
        dates = [datetime.today() - timedelta(days=i) for i in range(days)][::-1]
        regions = ["North America", "Europe (OECD)", "Asia-Pacific", "Middle East"]
        records = []
        for idx, dt in enumerate(dates):
            sf = np.sin(2 * np.pi * idx / 365.0)
            crude = 78.5 + 8.0 * sf + np.random.normal(0, 1.8)
            gas = max(1.2, 2.85 + 0.65 * sf + np.random.normal(0, 0.15))
            for reg in regions:
                mult = {"North America": 1.2, "Europe (OECD)": 0.9, "Asia-Pacific": 1.5, "Middle East": 0.6}[reg]
                demand = (11500 * mult) + (1400 * sf * mult) + np.random.normal(0, 220)
                renew = np.clip(32.0 + (idx * 0.015) + np.random.normal(0, 2.5), 5.0, 85.0)
                carbon = np.clip(450 - (renew * 3.8) + np.random.normal(0, 10), 80, 700)
                sent = np.clip(np.random.normal(0.08, 0.35), -0.95, 0.95)
                row = EnergyRecordSchema(
                    report_date=dt.strftime("%Y-%m-%d"), region=reg,
                    brent_crude_usd=round(float(crude), 2), henry_hub_gas_usd=round(float(gas), 2),
                    electricity_demand_gwh=round(float(demand), 2), renewable_share_pct=round(float(renew), 2),
                    carbon_intensity_gco2=round(float(carbon), 2), ai_sentiment_score=round(float(sent), 3)
                ).model_dump()
                row["data_quality_flag"] = "VALIDATED"
                records.append(row)
        df = pd.DataFrame(records)
        conn = sqlite3.connect(self.db_path)
        df.to_sql("energy_market_metrics", conn, if_exists="replace", index=False)
        conn.close()
        logging.info(f"Loaded {len(df)} validated records into SQL database.")

if __name__ == "__main__":
    EnergyETLPipeline().run_pipeline()
