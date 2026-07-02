# DataFlow Analytics Pipeline
## Project Overview

DataFlow Analytics Pipeline is an end-to-end ETL project that simulates a real-world data engineering workflow. It ingests product data from a REST API, processes and validates the data, stores it in a PostgreSQL database using a staged architecture, and visualises key business insights through an interactive dashboard.

This project demonstrates core data engineering concepts including API ingestion, transformation logic, data quality checks, and incremental loading.

Key learnings taken from my initial [ETL Pipeline project](https://github.com/AnoukDunu/ETL-Pipeline) have been acknowledged and implemented here!

## Project Features

- End-to-end ETL pipeline
- Modular project structure
- Data transformation using Pandas
- PostgreSQL database integration
- Data quality checks before loading
- Centralised logging system
- REST API based data ingestion/extraction
- Dashboard for interactive data visualisation

## Pipeline Architecture

API → Extract → Staging Table → Transform → Quality Checks → Final Table → Dashboard


## Project Structure
<img width="1136" height="1252" alt="image" src="https://github.com/user-attachments/assets/0b61cf55-5757-40f9-a9d6-240ce45d5221" />

## Tech Stack
- Python
- PostgreSQL
- Streamlit
- REST API


## Setup Instructions (Mac)
1. Clone the repository
```
git clone https://github.com/AnoukDunu/DataFlow-Analytics-Pipeline.git
cd DataFlow-Analytics-Pipeline
```
2. Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Configure environment variables in .env
```
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

5. Set up PostgreSQL database (schema found in 'src/database/database schema') by pasting in psql terminal\
Staging Table Schema:
```
CREATE TABLE stg_products (
    id INT,
    title VARCHAR(255),
    price DECIMAL(10, 2),
    description TEXT,
    category VARCHAR(255),
    image VARCHAR(255),
    rating JSONB,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
Final Table schema:
```
CREATE TABLE cln_products (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    price DECIMAL(10, 2),
    description TEXT,
    category VARCHAR(255),
    image VARCHAR(255),
    rating_rate FLOAT,
    rating_count INTEGER,
    estimated_revenue FLOAT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

6. Run the ETL pipeline
```
python main.py
```
7. Run the Streamlit dashboard (Check troubleshooting notes below)\
```
PYTHONPATH=src streamlit run dashboard/app.py
```
## Screenshots:
<img width="407" height="703" alt="Screenshot 2026-06-19 at 4 36 53 pm" src="https://github.com/user-attachments/assets/7b61bf15-14e8-43a7-8d97-a1478f09eab5" />

## Future Improvements:
- Implement Airflow to orchestrate the ETL pipeline (within a Docker container due to MacOS restrictions)
- Add unit and integrations tests using pytest
- Design data transform logic to be more modular
- Aim to create a more customisable streamlit dashboard with:
  - Login functionality
  - Use multiple data sources (API, CSV etc.) to extract and transform data
  - Include the functionality to create database schemas from within the ETL Dashboard
  - Host the entire pipeline on a server
  - Incorporate the pipeline into a larger data warehousing project    
  

## Troubleshooting:
- Due to a pathing issue (which will be fixed later on), to run the code and view the streamlit dashboard, run the following terminal command from the project root: 
```
PYTHONPATH=src streamlit run dashboard/app.py
```
- If you get the following error on MacOS, a manual clean installation of numpy will need to be done inside the virtual environment.\n
 Error Message:
```
"collections.cpython-39-darwin.so Not Opened ex Apple could not verify collections.cpython-39- ne. darwin.so is free of malware that may harm your Mac or compromise your privacy."
```
Clean numpy install:
```
pip uninstall numpy -y

pip install --force-reinstall numpy
```
However, you may still get an error in the terminal when running 'python main.py'. You can click through the errors and still pipeline.

In MacOS, the following can be done to avoid this error as well:
<img width="706" height="203" alt="Screenshot 2026-07-02 at 4 38 27 pm" src="https://github.com/user-attachments/assets/5f41b4a8-1603-44ef-a21b-0ed68af5a2a4" />

