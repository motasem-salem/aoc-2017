import sys

input = '10 3 15  10  5 15  5 15  9 2 5 8 5 2 3 6'

banks = list(map(int, input.split()))
ll = len(banks)
part1, part2 = 0, 0
seen = set(tuple(banks))
part2_start = None
while True:
  max_bank = max(banks)
  max_index = banks.index(max_bank)
  i = 1
  banks[max_index] = 0
  while max_bank > 0:
    banks[(max_index + i) % ll] += 1
    i += 1
    max_bank -= 1
  part1 += 1
  if part2_start:
    part2 += 1
    if tuple(banks) == part2_start:
      print(part2)
      break  
  elif tuple(banks) in seen:
    print(part1)
    part2_start = tuple(banks)
  else:
    seen.add(tuple(banks))
