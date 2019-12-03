with open('./input1.txt', 'r') as file:
    listInt = file.readline().split(",")
    listInt = list(map(int, listInt))
    print("========== INPUT ==========")
    print(listInt)

    for i in range(0, len(listInt), 4):
        if listInt[i] == 99:
            print("Opcode 99, halting")
            break
        if listInt[i] != 1 and listInt[i] != 2 and listInt[i] != 99:
            print("Something went wrong!")
            break
        firstAfterCurr = listInt[i+1] # grab the value at listInt[i+1], i+2, i+3
        secondAfterCurr = listInt[i+2]
        thirdAfterCurr = listInt[i+3]

        # Replace at the position of the values grabbed from above 
        if listInt[i] == 1:
            listInt[thirdAfterCurr] = listInt[firstAfterCurr] + listInt[secondAfterCurr]
        if listInt[i] == 2:
            listInt[thirdAfterCurr] = listInt[firstAfterCurr] * listInt[secondAfterCurr]
            
    print("========== OUTPUT ==========")
    print(listInt)
    print("With position 1 == 12, and position 2 == 2, the value at position 0 is " + str(listInt[0]))