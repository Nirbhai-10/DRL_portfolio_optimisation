import pandas as pd
import os

# Directories where the stock and bond data CSV files are stored
stocks_directory = '/Users/nirbhaiverma/Desktop/PAPERS RESEARCH/Portfolio Opt ML-Sarkar IIM Ranchi/Data/training data/stocks/'
bonds_directory = '/Users/nirbhaiverma/Desktop/PAPERS RESEARCH/Portfolio Opt ML-Sarkar IIM Ranchi/Data/training data/bonds/'

# List of stock data files (modify if needed based on your file names)
stock_files = [
    'INFY.NS_data.csv', 'BSOFT.NS_data.csv', 'BBOX.NS_data.csv', 'ACCELYA.NS_data.csv',
    'HBLPOWER.NS_data.csv', 'BOSCHLTD.NS_data.csv', 'NCC.NS_data.csv', 'AUROPHARMA.NS_data.csv',
    'NATCOPHARM.NS_data.csv', 'SHRIRAMFIN.NS_data.csv', 'HINDUNILVR.NS_data.csv', 'SBIN.NS_data.csv',
    'DRREDDY.NS_data.csv', 'BHARTIARTL.NS_data.csv', 'ONGC.NS_data.csv'
]

# List of bond data files (excluding corporate bonds)
bond_files = ['IN5Y_data.csv', 'IN10Y_data.csv']

# Dictionary to hold all data
data = {}

# Read stock data files and store in the dictionary
for stock_file in stock_files:
    stock_name = stock_file.split('.')[0]  # Extract stock name from file name
    file_path = os.path.join(stocks_directory, stock_file)
    data[stock_name] = pd.read_csv(file_path, index_col='Date', parse_dates=True)

# Read bond data files and store in the dictionary
for bond_file in bond_files:
    bond_name = bond_file.split('_')[0]  # Extract bond name from file name
    file_path = os.path.join(bonds_directory, bond_file)
    data[bond_name] = pd.read_csv(file_path, index_col='Date', parse_dates=True)

# Ensure consistent date format parsing
for key in data:
    data[key].index = pd.to_datetime(data[key].index, format='%d/%m/%Y')

# Check for column names and handle missing 'Adj Close'
for key in data:
    if 'Adj Close' not in data[key].columns:
        data[key]['Adj Close'] = data[key].iloc[:, 0]  # Assume first column is the required data if 'Adj Close' is missing

# Create a combined DataFrame for all assets based on Adjusted Close prices
combined_data = pd.DataFrame({asset: data[asset]['Adj Close'] for asset in data})

# Save the combined data as a CSV file
combined_file_path = '/Users/nirbhaiverma/Desktop/PAPERS RESEARCH/Portfolio Opt ML-Sarkar IIM Ranchi/Data/combined_portfolio_data.csv'
combined_data.to_csv(combined_file_path)

print(combined_data.head())
print(f"Combined portfolio data saved to {combined_file_path}")