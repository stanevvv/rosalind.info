rabbit_pairs = 1

raw_input = input()
reproduction_months, newborn_pairs_each_month = [int(x) for x in raw_input.split()]

archive_of_pairs = [1, 1]
month = 1


while (month <= reproduction_months):
  if (month == 1 or month == 2):
    month += 1
    continue
  
  archive_of_pairs.append(archive_of_pairs[month - 2] + (archive_of_pairs[month - 3] * newborn_pairs_each_month))
  
  month += 1

print(archive_of_pairs[month - 2])
