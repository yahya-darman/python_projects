import pandas as pd

def load_data(file_path):
    """
    Load transportation data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: DataFrame containing the transportation data.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """
    Clean the transportation data by checking for missing values.
    
    Args:
        data (pd.DataFrame): DataFrame containing the transportation data.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Check for missing values
    if data.isnull().sum().any():
        print("Missing values found. Filling with zeros.")
        data.fillna(0, inplace=True)
    
    return data
