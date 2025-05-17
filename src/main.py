# src/main.py

import pandas as pd

# Load dataset
df = pd.read_csv("dataset/1000_ml_jobs_us.csv")

# Show basic info
print("Shape:", df.shape)
print(df.head())
print("Columns:", df.columns.tolist())

# Check for missing values
print(df.isnull().sum())
