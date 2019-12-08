RANGE1 = 124075
RANGE2 = 580770

# Transform @param num into int array
# iteratively check if each element has an identical neighbour
# Return True immediately if found, presence of more identical neighbors ignored
def checkAdjacent(num: int) -> bool:

    arr = list(map(int, str(num)))

    for j in range(len(arr) - 2):
        if arr[j] == arr[j+1]:
            if arr[j] != arr[j+2]:
                return True
            if arr[j] == arr[j+2]:
                return False
    return False

    
# Create 2 copies of @param num, and transform them into int arrays
# If sorting one does not change the array structure, 
# it means they were initially sorted
def checkIncreasing(num: int) -> bool:
    expectedArr = list(map(int, str(num)))
    arr = list(map(int, str(num)))

    if sorted(arr) == expectedArr:
        return True
    else:
        return False


def foo():
    numPossibilities = 0
    for i in range(RANGE1, RANGE2):
        if checkAdjacent(i) and checkIncreasing(i): # If both conditions are satisfied, it is a possible password
            numPossibilities = numPossibilities + 1
    print(numPossibilities)



def main():
    print(checkAdjacent(112233)) # true
    print(checkAdjacent(111222)) # false
    print(checkAdjacent(112223)) # true
    print(checkAdjacent(112222)) # true
    print(checkAdjacent(123444)) # false
    print(checkAdjacent(111122)) # true
    foo()

if __name__ == '__main__':
    main()