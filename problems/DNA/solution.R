library(stringr)

cat("Enter DNA String: ")
dna_string <- readLines(file("stdin"), n = 1)

cat(c("A: ", str_count(dna_string, "A"),
      "C: ", str_count(dna_string, "C"),
      "G: ", str_count(dna_string, "G"),
      "T: ", str_count(dna_string, "T"),
      "\n"))