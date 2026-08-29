library(stringr)

cat("DNA string: ")
dna_string <- readLines(file("stdin"), n = 1)

cat("RNA string:", str_replace_all(dna_string, "T", "U"), "\n")