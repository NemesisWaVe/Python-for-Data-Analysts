# intro_to_pandas.py

import pandas as pd

# --- What is Pandas? ---
# Pandas is the most popular library for data manipulation and analysis in Python.
# It provides data structures and functions needed to work with structured data seamlessly.
# The primary data structure in Pandas is the DataFrame.

# --- What is a DataFrame? ---
# A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet, a SQL table, or a dictionary of Series objects.

# --- Creating a DataFrame ---
# You can create a DataFrame from a dictionary.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

print("--- Our First DataFrame ---")
print(df)


# --- Reading Data from a File ---
# In the real world, you'll usually read data from files like CSVs or Excel sheets.
# Let's imagine we have a CSV file named 'sales_data.csv'.
# To read it, you would use:
# sales_df = pd.read_csv('sales_data.csv')
# For this example, let's create a sample CSV file first.
sample_csv_data = """product_id,sale_date,sale_amount
101,2023-01-15,150.50
102,2023-01-16,200.00
101,2023-01-17,155.00
103,2023-01-17,300.75
102,2023-01-18,210.25
"""
with open('sales_data.csv', 'w') as f:
    f.write(sample_csv_data)

# Now, let's read the CSV we just created.
sales_df = pd.read_csv('sales_data.csv')
print("\n--- DataFrame from a CSV file ---")
print(sales_df)


# --- Basic DataFrame Operations ---

# 1. Viewing the data
print("\n--- Viewing Data ---")
print("First 3 rows (.head()):")
print(sales_df.head(3))

print("\nLast 2 rows (.tail()):")
print(sales_df.tail(2))

print("\nDataFrame Info (.info()):")
sales_df.info()


# 2. Selecting Columns
print("\n--- Selecting a Single Column ---")
product_column = sales_df['product_id']
print(product_column)

print("\n--- Selecting Multiple Columns ---")
# Note the double square brackets
details_columns = sales_df[['product_id', 'sale_amount']]
print(details_columns)


# 3. Basic Filtering
print("\n--- Filtering Data ---")
# Get all sales where the amount was greater than 200
high_sales = sales_df[sales_df['sale_amount'] > 200]
print(high_sales)

# 4. Check for duplicates and remove them
df1 = pd.concat([df, df]) # Concatenate df with itself
print('Dimensions of the original frame:', df.shape)
print('Dimensions of the frame with duplicates:', df1.shape)

# 5. Remove duplicates
df1 = df1.drop_duplicates() # or use: df1.drop_duplicates(inplace=True)
print('Dimensions of the frame after removing duplicates:', df1.shape)

# 6. Change all column names to Upper case
df.columns = [i.upper() for i in df]
print(df.columns)

# 7. Handling missing values
df.isna().sum()
#df.isnull().sum()
#print(df.isnull())
print('The no. of nulls in each column is \n',df.isnull().sum())
df.dropna(axis = 1, inplace = False)

#Sort in ascending order of sale_amount and store the result in another frame
df1 = sales_df.copy()
df1['sale_date'] = pd.to_datetime(df1['sale_date'])
df1.sort_values("sale_date", inplace=True)
print(df1)

