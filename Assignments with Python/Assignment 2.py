import pandas as pd

url = "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df = pd.read_csv(url)

# Task 1: Create new column 'Average Score'
df['Average Score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3

# Task 2: Apply a condition -> Pass/Fail
df['Result'] = df['Average Score'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# Check the result
print(df[['math score', 'reading score', 'writing score', 'Average Score', 'Result']].head())

# Bonus: count how many passed vs failed
print(df['Result'].value_counts())