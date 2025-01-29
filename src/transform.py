import pandas as pd

def transform_data():
    # Load the raw data
    df = pd.read_csv("data/raw_data/ecommerce_data.csv")
    
    # Data Cleaning: Remove rows with missing values
    df.dropna(inplace=True)

    # Feature Engineering: Add a new column for total price (quantity * price)
    df['total_price'] = df['quantity'] * df['price']

    # Feature Engineering: Convert 'order_date' to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Display the first few rows of the transformed data for verification
    print("Transformed Data:")
    print(df.head())

    # Save the cleaned and transformed data
    df.to_csv('data/processed_data/ecommerce_transformed.csv', index=False)
    print("Data transformation completed successfully!")

if __name__ == "__main__":
    transform_data()
