
import numpy as np
import pandas as pd

numbers = np.array([10, 20, 30, 40, 50])

print("NumPy Array:", numbers)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))

data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
