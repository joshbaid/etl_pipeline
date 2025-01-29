import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def load_data():
    # Read the transformed data
    df = pd.read_csv("data/processed_data/ecommerce_transformed.csv")
    
    # Connect to PostgreSQL
    engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/ecommerce_db")
    
    # Load data into PostgreSQL table
    df.to_sql('orders', engine, index=False, if_exists='replace')
    print("Data loaded successfully!")

if __name__ == "__main__":
    load_data()
