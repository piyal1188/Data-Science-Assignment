url <- "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df <- read.csv(url)

# Task 1: Create new column 'Average Score'
df$Average.Score <- (df$math.score + df$reading.score + df$writing.score) / 3

# Task 2: Apply a condition -> Pass/Fail
df$Result <- ifelse(df$Average.Score >= 60, "Pass", "Fail")

# Check the result
head(df[, c("math.score", "reading.score", "writing.score", "Average.Score", "Result")])

# Bonus: count how many passed vs failed
table(df$Result)