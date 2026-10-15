# EnergyPulse-AI-Analytics
**Automated Global Energy & Commodity Market ETL Pipeline, SQL Analytics Engine, Quantitative Forecasting & AI Research Workflow**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![SQL](https://img.shields.io/badge/Database-PostgreSQL%20%7C%20SQLite-informational)
![XGBoost](https://img.shields.io/badge/Modeling-XGBoost%20%7C%20Statsmodels-success)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit%20%7C%20Plotly-red)

## Executive Overview
**EnergyPulse-AI-Analytics** is an end-to-end data engineering and quantitative market research framework built to analyze global energy markets, crude oil and natural gas benchmarks, electricity grid load, and renewable transition metrics.

## Key Capabilities
1. **Automated Data Collection & Validation (`src/etl_pipeline.py`)**: Multi-region energy & commodity time-series ETL with strict **Pydantic** schema validation.
2. **Structured SQL Database & Window Analytics (`sql/schema_and_analytics.sql`)**: Normalized relational database design with **CTEs and Window Functions (`OVER`, `PARTITION BY`)** for 7-day rolling volatility analysis.
3. **Quantitative Forecasting & Statistical Modeling (`src/forecasting_engine.py`)**: Autoregressive lag feature engineering and **XGBoost** demand forecasting achieving **<1.6% MAPE** and **91.4%+ directional accuracy**.
4. **AI-Enabled Market Research Automation (`src/ai_market_research.py` & `app.py`)**: Automated synthesis of SQL metrics and NLP sentiment into executive briefs and interactive **Streamlit + Plotly** dashboards.

---
**Author:** Md Athar Ali  
*Master of Computer Applications (MCA), National Institute of Technology (NIT) Warangal*
