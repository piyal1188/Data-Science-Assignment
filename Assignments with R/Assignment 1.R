# Task: Load a CSV dataset (from the internet)
url <- "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df <- read.csv(url)

# Task: Display first 5 rows
cat("First 5 rows:\n")
print(head(df, 5))

# Task: Show column names
cat("\nColumn names:\n")
print(colnames(df))

# Task: Display number of rows and columns
cat("\nRows:", nrow(df), " Columns:", ncol(df), "\n")

# Task: Show summary statistics
cat("\nSummary statistics:\n")
print(summary(df))