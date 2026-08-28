# Define a named vector (a dictionary-like structure), containing all 64 possible codons
# name = codon
# value = amino acid
rna_codon_table <- c(
  UUU = "F", UUC = "F", UUA = "L", UUG = "L",
  CUU = "L", CUC = "L", CUA = "L", CUG = "L",
  AUU = "I", AUC = "I", AUA = "I", AUG = "M",
  GUU = "V", GUC = "V", GUA = "V", GUG = "V",
  UCU = "S", UCC = "S", UCA = "S", UCG = "S",
  CCU = "P", CCC = "P", CCA = "P", CCG = "P",
  ACU = "T", ACC = "T", ACA = "T", ACG = "T",
  GCU = "A", GCC = "A", GCA = "A", GCG = "A",
  UAU = "Y", UAC = "Y", UAA = "Stop", UAG = "Stop",
  CAU = "H", CAC = "H", CAA = "Q", CAG = "Q",
  AAU = "N", AAC = "N", AAA = "K", AAG = "K",
  GAU = "D", GAC = "D", GAA = "E", GAG = "E",
  UGU = "C", UGC = "C", UGA = "Stop", UGG = "W",
  CGU = "R", CGC = "R", CGA = "R", CGG = "R",
  AGU = "S", AGC = "S", AGA = "R", AGG = "R",
  GGU = "G", GGC = "G", GGA = "G", GGG = "G"
)

# User inputs an genetic string, corresponding to a strand of mRNA (messenger RNA)
rna_sequence <- readline(prompt = "Enter RNA sequence: ")

# Validate RNA sequence length is divisible by 3
if (nchar(rna_sequence) %% 3 != 0) {
  stop("RNA sequence length must be divisible by 3.")
}

# Validate RNA sequence contains only the four nucleotides {A, C, G, U}
if (!grepl("^[ACGU]+$", rna_sequence)) {
  stop("RNA sequence must contain only A, C, G, and U.")
}

# Define empty protein sequence, we will populate it incrementally
protein_sequence <- ""

# Iterate over the starting indexes of each codon (1, 4, 7, ... , <length of RNA>)
for (starting_codon_index in seq(1, nchar(rna_sequence), by = 3)) {
  # Extract the next codon
  codon <- substr(rna_sequence, starting_codon_index, starting_codon_index + 2)

  # Stop translation if a stop codon is encountered
  if (rna_codon_table[codon] == "Stop") {
    break
  }
  # Append to protein_sequence the amino acid, corresponding to the codon
  protein_sequence <- paste0(protein_sequence, rna_codon_table[codon])
}

# Final output
cat("Protein sequence: ", protein_sequence, "\n")