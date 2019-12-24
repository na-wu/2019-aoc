import math

with open("./input1.txt", "r") as file:
    listInt = file.readline()
    listInt = list(map(int, listInt))

dimensions = 6 * 25
numLayers = int(len(listInt)/dimensions)

def stack(top, bottom):
  for i in range(len(top)):
    if top[i] == 2:
      top[i] = bottom[i]
  return top

image = []
for i in range(0,numLayers):
  layer = []
  for j in range(0,dimensions):
    layer.append(listInt.pop(0))
  image.append(layer)


# Copy Layer 1 and iteratively stack them above the following layers
# Only replacing the transparent ones
curr = image[0].copy()
for i in range(1,len(image)):
  curr = stack(curr, image[i])


# Replace all 1's with #
# Replace all 0's with " " space
for i in range(len(curr)):
  if curr[i] == 1:
    curr[i] = "#"
  if curr[i] == 0:
    curr[i] = " "

# Split into a 25 x 6 matrix to output code
def code():
    for i in range(0,len(curr),25):
        s = [str(i) for i in curr[i:i+24]]
        print("".join(s))

print("The answer to Part 2 is: ")
code()