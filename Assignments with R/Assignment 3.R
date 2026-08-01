url <- "https://raw.githubusercontent.com/rashida048/Datasets/master/StudentsPerformance.csv"
df <- read.csv(url)

# Task: Sort data by a specific column (ascending)
df_sorted <- df[order(df$math.score), ]

head(df_sorted[, c("math.score", "reading.score", "writing.score")])