dna_string = input()[::-1]

for nt in dna_string:
  if (nt == 'A'):
    print('T', end='')
  elif (nt == 'G'):
    print('C', end='')
  elif (nt == 'C'):
    print('G', end='')
  elif (nt == 'T'):
    print('A', end='')

print()