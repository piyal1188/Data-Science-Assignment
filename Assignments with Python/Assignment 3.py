import pandas as pd

url = "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df = pd.read_csv(url)

# Task: Sort data by a specific column (ascending)
df_sorted = df.sort_values(by='math score', ascending=True)

print(df_sorted[['math score', 'reading score', 'writing score']].head())