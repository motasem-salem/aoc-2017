from itertools import *

with open('day_02.input') as f:
  rows = [list(map(int, line.strip().split('\t'))) for line in f.readlines()]
 
def row_result(l):
  pairs = permutations(l, 2)
  for p in pairs:
    return([p[0] / p[1] for p in pairs if p[0] % p[1] == 0][0])

print(sum([max(r) - min(r) for r in rows]))
print(sum([row_result(r) for r in rows]))

