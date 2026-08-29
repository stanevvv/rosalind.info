library(stringr)

cat("DNA string 1: ")
dna1 <- readLines(file("stdin"), n = 1)

cat("DNA string 2: ")
dna2 <- readLines(file("stdin"), n = 1)

# Construct a regex that checks for overlapping occurunces of dna2
pattern <- paste0("(?=", dna2, ")")

# Get a list of integer matrices, containing start and end indicies of each occurence of dna2
matches <- str_locate_all(dna1, pattern)[[1]]

# Extract only the start index of each occurence of dna2
positions <- matches[, "start"]

cat(positions, "\n")