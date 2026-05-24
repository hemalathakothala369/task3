import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display dataset
print("Dataset:")
print(df)

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values and duplicates
df = df.dropna()
df = df.drop_duplicates()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Statistical summary
print("\nStatistics:")
print(df.describe())

# Filter high sales
high_sales = df[df['Sales'] > 500]

print("\nHigh Sales Products:")
print(high_sales)

# Group by category
category_sales = df.groupby('Category')['Sales'].sum()

print("\nCategory Wise Sales:")
print(category_sales)

# Average sales
avg_sales = df['Sales'].mean()

print("\nAverage Sales:", avg_sales)

# Top selling category
top_category = category_sales.idxmax()

print("\nTop Selling Category:", top_category)

# Visualization
category_sales.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()