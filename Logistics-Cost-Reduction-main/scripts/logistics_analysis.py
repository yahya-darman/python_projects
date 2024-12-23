import pandas as pd

def identify_high_cost_routes(data):
    """
    Identify high-cost routes based on transportation cost.
    
    Args:
        data (pd.DataFrame): DataFrame containing transportation data.
        
    Returns:
        pd.DataFrame: DataFrame with high-cost routes identified.
    """
    high_cost_threshold = data['transportation_cost'].mean()
    high_cost_routes = data[data['transportation_cost'] > high_cost_threshold]
    return high_cost_routes

def consolidate_shipments(data):
    """
    Consolidate shipments for identified high-cost routes.
    
    Args:
        data (pd.DataFrame): DataFrame containing transportation data.
        
    Returns:
        pd.DataFrame: DataFrame with consolidated shipment data.
    """
    # Example consolidation: Sum costs and volumes for high-cost routes
    consolidated_data = data.groupby('route_id').agg({
        'transportation_cost': 'sum',
        'shipment_volume': 'sum'
    }).reset_index()
    
    return consolidated_data

def main():
    # Load and clean the data
    file_path = '../data/transportation_data.csv'  # Adjust the path as necessary
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    
    # Identify high-cost routes
    high_cost_routes = identify_high_cost_routes(cleaned_data)
    
    # Consolidate shipments
    consolidated_data = consolidate_shipments(high_cost_routes)
    
    # Print results
    print("High-Cost Routes:")
    print(high_cost_routes)
    
    print("\nConsolidated Shipment Data:")
    print(consolidated_data)

if __name__ == "__main__":
    main()
