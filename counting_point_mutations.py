dna1 = input()
dna2 = input()

point_mutations_count = 0
for iter1, iter2 in zip(dna1, dna2):
    if (iter1 != iter2):
        point_mutations_count += 1
        
print(point_mutations_count)