import sqlite3, numpy as np, pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
from xgboost import XGBRegressor

class EnergyForecastingModel:
    def __init__(self, db_path="data/energy_market.db"):
        self.db_path = db_path
        self.model = XGBRegressor(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)

    def train_and_evaluate(self, region="Asia-Pacific"):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM energy_market_metrics WHERE region = ? ORDER BY report_date ASC", conn, params=(region,))
        conn.close()
        for lag in [1, 3, 7, 14]:
            df[f"demand_lag_{lag}"] = df["electricity_demand_gwh"].shift(lag)
        df["rolling_mean_7"] = df["electricity_demand_gwh"].rolling(7).mean()
        df = df.dropna().reset_index(drop=True)
        features = ["brent_crude_usd", "henry_hub_gas_usd", "renewable_share_pct", "ai_sentiment_score", "demand_lag_1", "demand_lag_3", "demand_lag_7", "demand_lag_14", "rolling_mean_7"]
        split = int(len(df) * 0.85)
        train, test = df.iloc[:split], df.iloc[split:]
        self.model.fit(train[features], train["electricity_demand_gwh"])
        preds = self.model.predict(test[features])
        mape = mean_absolute_percentage_error(test["electricity_demand_gwh"], preds) * 100
        return {"region": region, "mape_pct": round(float(mape), 2)}

if __name__ == "__main__":
    print(EnergyForecastingModel().train_and_evaluate())
