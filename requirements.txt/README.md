# E-Commerce ETL Pipeline

## Project Overview

This project involves building an ETL pipeline to extract data from a simulated e-commerce API, transform it using Pandas, and load it into a PostgreSQL database. The pipeline is automated using Apache Airflow and deployed on AWS.

## Steps:

1. **Extract**: Data is pulled from a simulated e-commerce API and saved as a CSV file.
2. **Transform**: The data is cleaned and features are engineered using Pandas.
3. **Load**: The transformed data is loaded into a PostgreSQL database.
4. **Automation**: The entire pipeline is automated using Apache Airflow and deployed on AWS.

## Requirements

- Python 3.x
- PostgreSQL
- Apache Airflow
- AWS S3

## How to Run:

1. Set up your PostgreSQL database.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up and configure Airflow.
4. Run the Airflow DAG to start the ETL process.
