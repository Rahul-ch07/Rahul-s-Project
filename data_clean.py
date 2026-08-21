import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"R:\Rahul project\Python\emp-id-name-15.csv")
print(df.head())

print("-----MISSING VALUES-----")
print(df.isnull().sum())

# Handle missing values safely
df['Salary (NPR)'] = df['Salary (NPR)'].fillna(df['Salary (NPR)'].mean())
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

# Replace infinities with NaN, then fill numeric NaNs with column means
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.select_dtypes(include=[np.number]).mean(), inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Replace negative salaries with mean salary
df["Salary (NPR)"] = np.where(df["Salary (NPR)"] < 0,
                              df["Salary (NPR)"].mean(),
                              df["Salary (NPR)"])

# Handle outliers (3-sigma rule)
salary_mean = df["Salary (NPR)"].mean()
salary_std = df["Salary (NPR)"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df["Salary (NPR)"] >= lower_bound) & (df["Salary (NPR)"] <= upper_bound)]

# Save cleaned dataset
df.to_csv("emp-id-name-15.csv", index=False)
print('Data cleaning completed! File saved as "emp-id-name-15.csv"')
