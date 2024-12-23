import pandas as pd

def load_data(file_path):
    """
    Load inventory data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: DataFrame containing the inventory data.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """
    Clean the inventory data by checking for missing values.
    
    Args:
        data (pd.DataFrame): DataFrame containing the inventory data.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Check for missing values
    if data.isnull().sum().any():
        print("Missing values found. Filling with zeros.")
        data.fillna(0, inplace=True)
    
    return data

if __name__ == "__main__":
    # Example usage
    file_path = '../data/sample_data.csv'  # Adjust the path as necessary
    inventory_data = load_data(file_path)
    cleaned_data = clean_data(inventory_data)
    print(cleaned_data)
