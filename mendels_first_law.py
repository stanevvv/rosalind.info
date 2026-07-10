from math import comb

k, m, n = map(int, input().split())
population_size = k + m + n
total_possible_pairs = comb(population_size, 2)

number_of_k_with_k_pairs = comb(k, 2)
number_of_m_with_m_pairs = comb(m, 2)
number_of_n_with_n_pairs = comb(n, 2)
number_of_k_with_m_pairs = k * m
number_of_k_with_n_pairs = k * n
number_of_m_with_n_pairs = m * n


probability_offspring_has_dominant_allele = (number_of_k_with_k_pairs / total_possible_pairs) + (number_of_k_with_m_pairs / total_possible_pairs) + (number_of_k_with_n_pairs / total_possible_pairs) + (number_of_m_with_n_pairs / total_possible_pairs) * 0.5 + (number_of_m_with_m_pairs / total_possible_pairs) * 0.75

print(probability_offspring_has_dominant_allele)
# Given:
#   Three positive integers k, m, and n describe a population of:
#
#       k + m + n organisms
#
#   where:
#       k = number of homozygous dominant organisms (AA)
#       m = number of heterozygous organisms (Aa)
#       n = number of homozygous recessive organisms (aa)
#
# Goal:
#   Calculate the probability that two randomly selected organisms produce
#   an offspring with at least one dominant allele and therefore the
#   dominant phenotype.
#
# Assumption:
#   Any two distinct organisms in the population can mate.
#
#
# Variables and events:
#
#   population_size = k + m + n
#
#   A = event that the selected pair produces an offspring with the
#       dominant phenotype
#
#
# The mating pair is treated as unordered:
#
#       {AA, Aa} == {Aa, AA}
#
# We care only about which two organisms are selected, not the order in
# which they are selected.
#
# Therefore, the total number of possible mating pairs is:
#
#       C(k + m + n, 2)
#
# where C(N, 2), or "N choose 2", is the binomial coefficient.
# In Python, it can be calculated with:
#
#       math.comb(N, 2)
#
#
# For each possible parental genotype pairing, multiply:
#
#       probability of selecting that pair
#       ×
#       probability of dominant offspring given that pair
#
#
# The possible crosses and their probabilities of dominant offspring are:
#
#       AA × AA  -> 1.00
#       AA × Aa  -> 1.00
#       AA × aa  -> 1.00
#       Aa × Aa  -> 0.75
#       Aa × aa  -> 0.50
#       aa × aa  -> 0.00
#
#
# By the law of total probability:
#
#   P(A) =
#       P(AA, AA) × 1.00
#       + P(AA, Aa) × 1.00
#       + P(AA, aa) × 1.00
#       + P(Aa, Aa) × 0.75
#       + P(Aa, aa) × 0.50
#       + P(aa, aa) × 0.00
#
# Since the final term is multiplied by zero, it can be omitted:
#
#   P(A) =
#       P(AA, AA)
#       + P(AA, Aa)
#       + P(AA, aa)
#       + 0.75 × P(Aa, Aa)
#       + 0.50 × P(Aa, aa)
#
#
# The number of pairs of each type is:
#
#       AA, AA -> C(k, 2)
#       AA, Aa -> k × m
#       AA, aa -> k × n
#       Aa, Aa -> C(m, 2)
#       Aa, aa -> m × n
#       aa, aa -> C(n, 2)
#
# Each pair-selection probability is:
#
#       number of pairs of that type
#       --------------------------------
#       total number of possible pairs