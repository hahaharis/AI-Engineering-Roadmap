
import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("iris_cleaned.csv")

print("========== DATA ANALYSIS ==========")

# Finding 1: Total flowers
print("\n1. Total Flowers:")
print(len(df))

# Finding 2: Number of flowers per species
print("\n2. Flowers Per Species:")
print(df["species"].value_counts())

# Finding 3: Average measurements
print("\n3. Average Measurements:")
print(df.select_dtypes(include="number").mean())

# Finding 4: Average petal length per species
print("\n4. Average Petal Length Per Species:")
print(df.groupby("species")["petal_length"].mean())

# Finding 5: Correlation between measurements
print("\n5. Correlation Between Measurements:")
numeric_data = df.select_dtypes(include="number")
correlation = numeric_data.corr()

print(correlation)

# Additional NumPy analysis
petal_lengths = np.array(df["petal_length"])

print("\nNumPy Analysis:")
print("Maximum Petal Length:", np.max(petal_lengths))
print("Minimum Petal Length:", np.min(petal_lengths))
print("Standard Deviation:", np.std(petal_lengths))
