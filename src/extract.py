import requests
import pandas as pd
import os

def extract_data():
    url = "https://api.mocki.io/v1/abcd1234"  # Simulated API for e-commerce data
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        
        # Save the raw data to a CSV file for future use
        if not os.path.exists('data/raw_data'):
            os.makedirs('data/raw_data')
        df.to_csv('data/raw_data/ecommerce_data.csv', index=False)
        return df
    else:
        print("Failed to fetch data.")
        return None

if __name__ == "__main__":
    extract_data()
