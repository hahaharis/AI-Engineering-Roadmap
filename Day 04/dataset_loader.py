
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

# Load dataset
df = pd.read_csv(url)

# Inspect dataset
print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nDATASET INFORMATION:")
print(df.info())

print("\nSTATISTICAL SUMMARY:")
print(df.describe())
