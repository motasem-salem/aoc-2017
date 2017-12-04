# python day_04.py < day_04.input

from collections import Counter

answer1, answer2 = 0, 0

def is_valid(l):
  return(Counter(l).most_common(1)[0][1] == 1)

while True:
  words = input().split()
  answer1 += is_valid(words)
  words = [''.join(sorted(w)) for w in words]
  answer2 += is_valid(words)
  print(answer1, answer2)
