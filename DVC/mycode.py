import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = { 'Name': 'David', 'Age': 28, 'City': 'San Francisco' }
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = { 'Name': 'Eve', 'Age': 22, 'City': 'Miami' }
df.loc[len(df.index)] = new_row_loc2

# Ensure "data" directory exists at root level
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Define file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save DataFrame to CSV, including column headers
df.to_csv(file_path, index=False)

# Print confirmation message
print(f"DataFrame saved to {file_path}")




