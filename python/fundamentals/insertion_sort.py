def insertionSort(myList):
    for i in range(0,len(myList)):
        min = myList[i]
        newminindex = -1
        for j in range(i,-1,-1):
            if myList[j] > min:
                newminindex = j
        if newminindex != -1:
            temp = myList[i]
            myList.pop(i)
            myList.insert(newminindex,temp)
    return myList
print(insertionSort([2,3,4,5,5]))
