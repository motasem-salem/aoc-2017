mem = [int(i) for i in open('day_05.input')]

i, steps = 0, 0
while i < len(mem):
  steps += 1
  mem[i] += 1
  i += mem[i] - 1
    
print(steps)

mem = [int(i) for i in open('day_05.input')]
i, steps = 0, 0
while i < len(mem):
  steps += 1
  inc = -1 if mem[i] >= 3 else 1
  mem[i] += inc
  i += mem[i] - inc

print(steps)
