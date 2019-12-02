import math



def fuelOfOne(num: int) -> int:
  return math.floor(num/3) - 2

with open("./input1.txt", "r") as file:
  i = 1
  x = 0
  while(i == 1):
    line = file.readline()
    if line == '':
      break
    x = x + fuelOfOne(int(line))
    
print(x)

