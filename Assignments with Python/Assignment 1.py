import pandas as pd

# Task: Load a CSV dataset (from the internet)
url = "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df = pd.read_csv(url)

# Task: Display first 5 rows
print("First 5 rows:")
print(df.head())
# Task: Show column names
print("\nColumn names:")
print(df.columns.tolist())
# Task: Display number of rows and columns
print("\nRows and Columns:", df.shape)
# Task: Show summary statistics
print("\nSummary statistics:")
print(df.describe())
