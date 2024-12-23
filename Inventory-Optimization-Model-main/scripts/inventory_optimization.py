import pandas as pd

def calculate_reorder_level(data):
    """
    Calculate the optimal reorder level for each product.
    
    Args:
        data (pd.DataFrame): DataFrame containing inventory data.
        
    Returns:
        pd.DataFrame: DataFrame with reorder levels added.
    """
    # Assuming a basic reorder level formula: average_demand * lead_time
    data['reorder_level'] = data['average_demand'] * data['lead_time']
    return data

def identify_excess_inventory(data):
    """
    Identify products with excess inventory.
    
    Args:
        data (pd.DataFrame): DataFrame containing inventory data.
        
    Returns:
        pd.DataFrame: DataFrame with excess inventory identified.
    """
    data['excess_inventory'] = data['current_inventory'] - data['reorder_level']
    return data[data['excess_inventory'] > 0]

def main():
    # Load and clean the data
    file_path = '../data/sample_data.csv'  # Adjust the path as necessary
    data = pd.read_csv(file_path)
    
    # Calculate reorder levels
    data = calculate_reorder_level(data)
    
    # Identify excess inventory
    excess_inventory = identify_excess_inventory(data)
    
    # Print results
    print("Inventory Data with Reorder Levels:")
    print(data[['product_id', 'current_inventory', 'average_demand', 'lead_time', 'reorder_level', 'excess_inventory']])
    
    print("\nProducts with Excess Inventory:")
    print(excess_inventory[['product_id', 'current_inventory', 'reorder_level', 'excess_inventory']])

if __name__ == "__main__":
    main()
