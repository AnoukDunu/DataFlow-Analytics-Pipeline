# DataFlow Analytics Pipeline
## Project Overview

DataFlow Analytics Pipeline is an end-to-end ETL project that simulates a real-world data engineering workflow. It ingests product data from a REST API, processes and validates the data, stores it in a PostgreSQL database using a staged architecture, and visualises key business insights through an interactive dashboard.

This project demonstrates core data engineering concepts including API ingestion, transformation logic, data quality checks, and incremental loading.

## Project Features

-- End-to-end ETL pipeline\
-- Modular project structure\
-- Data transformation using Pandas\
-- PostgreSQL database integration\
-- Data quality checks before loading\
-- Centralised logging system\
-- REST API based data ingestion/extraction\
-- Dashboard for interactive data visualisation\

## Pipeline Architecture

API → Extract → Staging Table → Transform → Quality Checks → Final Table → Dashboard


## Project Structure
<img width="1136" height="1252" alt="image" src="https://github.com/user-attachments/assets/0b61cf55-5757-40f9-a9d6-240ce45d5221" />

## Tech Stack
-- Python\
-- PostgreSQL\
-- Streamlit\
-- REST API\


## Setup Instructions (Mac)
1. Clone the repository
git clone <your-repo-url>
cd etl_pipeline_project

3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Configure environment variables

Create a .env file:

DB_HOST=localhost

DB_NAME=etl_db

DB_USER=postgres

DB_PASSWORD=yourpassword

DB_PORT=5432

5. Set up PostgreSQL database
Create database: etl_db
Create required tables (if not automated in load.py)

7. Run the ETL pipeline
python main.py

6. Run the Streamlit dashboard
streamlit run app.py

## Future Improvements:
Will write them when I think of any lol

## Troubleshooting:
Due to a pathing issue (which will be fixed later on), to run the code and view the streamlit dashboard, run the following terminal command from the project root: PYTHONPATH=src streamlit run dashboard/app.py
