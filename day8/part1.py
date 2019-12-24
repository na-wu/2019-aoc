import math

with open("./input1.txt", "r") as file:
    listInt = file.readline()
    listInt = list(map(int, listInt))

dimensions = 6 * 25
numLayers = int(len(listInt)/dimensions) # Total number of pixels / dimensions of each layer = # Layers

# Count the number of occurences of the value num
def checkNum(image, num):
  count = 0
  for i in range(len(image)):
    if image[i] == num:
      count += 1
  return count

image = []
# Create list and populate it with first 150 items, then append it to bigger list
for i in range(0,numLayers):
  layer = []
  for j in range(0,dimensions):
    layer.append(listInt.pop(0))
  image.append(layer)

currMax = checkNum(image[0], 0)
currMaxIdx = 0
# Initial number of 0s is the number in the first layer,
# Subsequent calls to checkNum should replace currMax if there are less 0s
# Set CurrMaxIdx to the index with the least number of 0s
for i in range(len(image)):
  curr = checkNum(image[i], 0)
  if curr < currMax:
    currMax = curr
    currMaxIdx = i

numOnes = checkNum(image[currMaxIdx], 1)
numTwos = checkNum(image[currMaxIdx], 2)
print("The answer to Part 1 is: " + str(numOnes * numTwos))
