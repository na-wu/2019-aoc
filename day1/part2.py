import math

def fuelOfOne(num: int) -> int:
    if num <= 6:
        return 0
    curr = math.floor(num/3) - 2
    return fuelOfOne(curr) + curr

with open("./input2.txt", "r") as file:
  x = 0
  while(True):
    line = file.readline()
    print(line)
    if line == '':
      break
    x = x + fuelOfOne(int(line))
    
print(x)

