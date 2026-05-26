import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/retail_sales_dataset.csv")

print("Original Data:")
print(df.head())

# -------------------------
# DATA CLEANING
# -------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with mean
numeric_cols = df.select_dtypes(include=['number']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing text values
text_cols = df.select_dtypes(include=['object']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned dataset
df.to_csv("data/cleaned_retail_sales.csv", index=False)

print("\nData Cleaning Completed!")

# -------------------------
# REPORT GENERATION
# -------------------------

# Example sales summary
if 'total_amount' in df.columns and 'product_category' in df.columns:

    summary = df.groupby('product_category')['total_amount'].sum()

    print("\nSales Summary:")
    print(summary)

    # Create bar chart
    summary.plot(kind='bar')

    plt.title("Sales by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Total Sales")

    plt.tight_layout()

    # Save chart
    plt.savefig("reports/sales_report.png")

    print("\nReport Generated Successfully!")

else:
    print("\nColumn names not matching dataset.")
    print("Available columns:")
    print(df.columns)