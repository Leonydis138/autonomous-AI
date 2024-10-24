import pandas as pd

def extract_data(source):
    return pd.read_csv(source)

def transform_data(df):
    # Example transformation: fill missing values
    df.fillna(method='ffill', inplace=True)
    return df

def load_data(df, destination):
    df.to_csv(destination, index=False)

# Example usage:
source = "input_data.csv"
destination = "processed_data.csv"
data = extract_data(source)
transformed_data = transform_data(data)
load_data(transformed_data, destination)
 
