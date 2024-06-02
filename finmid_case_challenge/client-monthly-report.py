# main_script.py
#!pip install pandas
#!pip install re


import pandas as pd
from db_connection import engine
import re

# Function to validate user input format
def validate_input(user_input):
    pattern = r'^\d{4}-\d{2}-01$'  # Regex pattern for YYYY-MM-01 format
    if re.match(pattern, user_input):
        return True
    else:
        return False

# Define the SQL query
query = """
    SELECT DATE_TRUNC('month',t.booked_time)::DATE as report_month,
                  t.client_name,
                  SUM(COALESCE(rate * revenue, revenue)) as eur_revenue
FROM transactions as t
LEFT JOIN exchange_rates as ex
ON ex.date =  t.booked_time::date
AND ex.buy_currency = 'EUR'
AND ex.sell_currency = currency 
GROUP BY 1,2
ORDER BY 1
"""
# Execute the query and read the result into a DataFrame
transactions = pd.read_sql_query(query, engine)

# Get input from the user and validate it
while True:
    user_input = input("Enter a date in the format [YYYY-MM-01] (or 'all' for all months): ")
    if user_input == 'all' or validate_input(user_input):
        break
    else:
        print("Input format is incorrect. Please enter a date in the format [YYYY-MM-01] or 'all'.")


# Load your transactions DataFrame (replace this with your actual DataFrame)
# transactions = pd.read_csv("transactions.csv")

# Assuming transactions DataFrame is already defined
# Perform actions based on user input
if user_input == 'all':
    # Define the path to save the CSV file
    csv_file_path = "client_monthly_report.csv"
    # Write the DataFrame to a CSV file 
    transactions.to_csv(csv_file_path, index=False) 
    print(f"CSV file '{csv_file_path}' has been created successfully.")
else:
    if validate_input(user_input):
        transactions = transactions[transactions['report_month'] == user_input]
        # Define the path to save the CSV file
        csv_file_path = f'client_monthly_report_{user_input}.csv'

        # Write the DataFrame to a CSV file 
        transactions.to_csv(csv_file_path, index=False) 
        print(f"CSV file '{csv_file_path}' has been created successfully.")
    else: 
        print("Input format is incorrect. Please enter a date in the format [YYYY-MM-01].")
