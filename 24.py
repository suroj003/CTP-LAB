import pandas as pd

df = pd.read_csv("titanic.csv")

print("Original Data:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("cleaned_titanic.csv", index=False)

print("\nDataset cleaned successfully!")