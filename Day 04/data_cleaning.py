
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

# 1. Check missing values
print("Missing values:")
print(df.isnull().sum())

# 2. Check duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())

# 3. Remove duplicate records
df = df.drop_duplicates()

# 4. Handle missing numerical values
for column in df.select_dtypes(include="number").columns:
    df[column] = df[column].fillna(df[column].mean())

# 5. Verify cleaned data
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal dataset shape:")
print(df.shape)

print("\nCleaned dataset:")
print(df.head())

# 6. Save cleaned dataset
df.to_csv("iris_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
