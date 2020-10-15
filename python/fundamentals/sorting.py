        ## SELECTION SORT
myList = [11,2,9,6,7]
for i in range(len(myList)):
    min = myList[i]
    newmin = myList[i]
    newminindex = 0
    for j in range(i,len(myList)):
        if min > myList[j]:
            min = myList[j]
            newminindex = j
    if newmin > min:
        newmin = min
        myList[newminindex] = myList[i]
        myList[i] = min
        
print(myList)


#       ## RECURSIVE BUBBLE SORT
# 
# def bubbleSort(myList,fromBack=0):
#     count = 0
    
#     for i in range(len(myList)-1-fromBack):
#         if myList[i] > myList[i+1]:
#             myList[i], myList[i+1] = myList[i+1], myList[i]
#             count += 1
#     if count >= 1:
#         myList = bubbleSort(myList, fromBack + 1)        
#     else:
#         return myList
#     return myList

        ## INNER LOOP BUBBLE SORT

# x = bubbleSort([1,4,6,3,5])
# print(x)

# myList = [1,2,4,6,7]
# count = False
# for i in range(len(myList)-1):
#     print(myList)
#     if count == False:
#         count = True
#         for j in range(len(myList)-1-i):
#             print(j)
#             if myList[j] > myList[j+1]:
#                 myList[j], myList[j+1] = myList[j+1], myList[j]
#                 count = False 
# print(myList)