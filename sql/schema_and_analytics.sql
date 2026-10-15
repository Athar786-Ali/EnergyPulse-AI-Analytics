-- EnergyPulse AI: Structured SQL Schema & Analytical Queries
CREATE TABLE IF NOT EXISTS energy_market_metrics (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_date DATE NOT NULL,
    region VARCHAR(50) NOT NULL,
    brent_crude_usd DECIMAL(10, 2),
    henry_hub_gas_usd DECIMAL(10, 2),
    electricity_demand_gwh DECIMAL(12, 2),
    renewable_share_pct DECIMAL(5, 2),
    carbon_intensity_gco2 DECIMAL(8, 2),
    ai_sentiment_score DECIMAL(4, 3),
    data_quality_flag VARCHAR(20) DEFAULT 'VALIDATED',
    UNIQUE(report_date, region)
);

-- 7-Day Rolling Volatility & Moving Average Query
SELECT report_date, region, brent_crude_usd, electricity_demand_gwh,
    ROUND(AVG(brent_crude_usd) OVER (PARTITION BY region ORDER BY report_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS brent_7d_ma,
    ROUND(AVG(electricity_demand_gwh) OVER (PARTITION BY region ORDER BY report_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS demand_7d_ma
FROM energy_market_metrics WHERE data_quality_flag = 'VALIDATED' ORDER BY report_date DESC;
