import pandas as pd

# Load the CSV file
df = pd.read_csv("sales_data.csv")

print("\n=== RAW DATA ===")
print(df)

print("\n=== TOTAL SALES BY PRODUCT ===")
print(df.groupby("product")["sales"].sum())

print("\n=== TOTAL SALES BY MONTH ===")
print(df.groupby("month")["sales"].sum())
