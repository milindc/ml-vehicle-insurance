import pandas as pd
import os

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

df = pd.DataFrame(data)

# Add new row to the DataFrame
new_row = {"Name": "Frank", "Age": 50, "City": "Philadelphia"}
df.loc[len(df.index)] = new_row

# # Add another new row to the DataFrame
# another_new_row = {"Name": "Grace", "Age": 28, "City": "San Francisco"}
# df.loc[len(df.index)] = another_new_row

file_path = os.path.join("data", "people_data.csv")

df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
