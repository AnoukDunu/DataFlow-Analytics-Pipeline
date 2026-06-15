# DataFlow-Analytics-Pipeline
#Project Overview

DataFlow Analytics Pipeline is an end-to-end ETL project that simulates a real-world data engineering workflow. It ingests product data from a REST API, processes and validates the data, stores it in a PostgreSQL database using a staged architecture, and visualises key business insights through an interactive dashboard.

This project demonstrates core data engineering concepts including API ingestion, transformation logic, data quality checks, and incremental loading.

Pipeline Architecture

API → Extract → Staging Table → Transform → Final Table → Dashboard

Extract: Pulls raw product data from an external API
Staging Layer: Stores raw, unprocessed data for traceability
Transform: Cleans data, handles duplicates, and computes business metrics
Final Layer: Stores analytics-ready structured data
Dashboard: Visualises insights using Streamlit
🛠️ Tech Stack
Python
pandas
PostgreSQL
SQLAlchemy
psycopg2
Streamlit
REST API (FakeStore API)

⚙️ Key Features

✅ API-based data ingestion

✅ Staging and dimensional data modelling

✅ Data transformation and cleaning with pandas

✅ Data quality checks (nulls, duplicates, validation rules)

✅ Incremental loading to avoid duplicate records

✅ Error handling and logging

✅ Interactive dashboard for analytics

Troubleshooting:
Due to a pathing issue (which will be fixed later on), to run the code and view the streamlit dashboard, run the following terminal command from the project root: PYTHONPATH=src streamlit run dashboard/app.py