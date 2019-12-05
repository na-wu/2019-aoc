def handleOp(arr: list, j: int, k: int) -> None:
    arr[1] = j
    arr[2] = k
    for i in range(0, len(arr)-1, 4):
        if arr[i] == 99:
            return
        if arr[i] != 1 and arr[i] != 2 and arr[i] != 99:
            print("Something went wrong!")
            return
        firstAfterCurr = arr[i+1] # grab the value at listInt[i+1], i+2, i+3
        secondAfterCurr = arr[i+2]
        thirdAfterCurr = arr[i+3]
        
        # Replace at the position of the values grabbed from above 
        if arr[i] == 1:
            arr[thirdAfterCurr] = arr[firstAfterCurr] + arr[secondAfterCurr]
        if arr[i] == 2:
            arr[thirdAfterCurr] = arr[firstAfterCurr] * arr[secondAfterCurr]

with open('./input1.txt', 'r') as file:
    listInt = file.readline().split(",")
    listInt = list(map(int, listInt))
    print("========== INPUT ==========")
    print(listInt)
    print("========== Solution ==========")
    def foo():
        for i in range(0,100):
            for k in range(0,100):
                copy = list(listInt)
                handleOp(copy, i, k)
                if copy[0] == 19690720:
                    print("The noun is " + str(i) + " and the verb is " + str(k) + " to produce the output of 19690720")
                    print("The soution is " + str(100 * i + k))
                    return
    foo()
                

    # print("========== OUTPUT ==========")
    # print(listInt)
    # print("With position 1 == 12, and position 2 == 2, the value at position 0 is " + str(listInt[0]))
