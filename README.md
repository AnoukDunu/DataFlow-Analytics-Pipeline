# DataFlow Analytics Pipeline
Project Overview

DataFlow Analytics Pipeline is an end-to-end ETL project that simulates a real-world data engineering workflow. It ingests product data from a REST API, processes and validates the data, stores it in a PostgreSQL database using a staged architecture, and visualises key business insights through an interactive dashboard.

This project demonstrates core data engineering concepts including API ingestion, transformation logic, data quality checks, and incremental loading.

🧠 Key Features
🔄 End-to-end ETL pipeline
🧩 Modular project structure
📦 Data transformation using Pandas
🛢️ PostgreSQL database integration
🔍 Data quality checks before loading
📝 Centralised logging system
🌐 Data access via REST API
📊 Dashboard for data visualisation

Pipeline Architecture

API → Extract → Staging Table → Transform → Quality Checks → Final Table → Dashboard

Project Structure
DataFlow-Analytics-Pipeline
│
├── data/                         # Optional: local test data
│
├── src/                          # Core pipeline code
│   │
│   ├── config/                   # Configuration management
│   │   └── config.py
│   │
│   ├── extract/                  # Data ingestion layer
│   │   └── extract.py
│   │
│   ├── transform/                # Data transformation logic
│   │   └── transform.py
│   │
│   ├── load/                     # Data loading logic
│   │   ├── load_staging.py
│   │   └── load_final.py
│   │
│   ├── database/                       # Database connection logic
│   │   └── connection.py
│   │
│   ├── utilities/                    # Reusable helpers
│   │   ├── logger.py
│   │   └── quality_checks.py
│   │
│   └── main.py                   # Pipeline orchestrator
│
├── dashboard/                    # Streamlit dashboard
│   └── app.py
│
├── .env                          # Environment variables
├── requirements.txt
└── README.md


🛠️ Tech Stack
Python
PostgreSQL
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

🔧 Setup Instructions (Mac)
1. Clone the repository
git clone <your-repo-url>
cd etl_pipeline_project
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file:

DB_HOST=localhost
DB_NAME=etl_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_PORT=5432
5. Set up PostgreSQL database
Create database: etl_db
Create required tables (if not automated in load.py)
6. Run the ETL pipeline
python main.py
6. Run the Streamlit dashboard
streamlit run app.py

Future Improvements:
Will write them when I think of any lol

Troubleshooting:
Due to a pathing issue (which will be fixed later on), to run the code and view the streamlit dashboard, run the following terminal command from the project root: PYTHONPATH=src streamlit run dashboard/app.py