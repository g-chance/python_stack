# #1
# def countDown(num):
#     myList = []
#     for num in range(num,-1,-1):
#         myList.append(num)
#     print(myList)
# countDown(100)
# #2
# def pNR(a,b):
#     print(a)
#     return b
# x = pNR(5,3)
# print(x)
# #3
# def firstPlusLen(myList):
#     sum = 0
#     sum += myList[0]
#     sum += len(myList)
#     return sum
# x = firstPlusLen([5,2,3,4,5,6])
# print(x)
# 4
def valuesGreaterThan2nd(myList):
    if(len(myList) < 2):
        return False
    # sum = 0
    newList = []
    for i in range(len(myList)):
        if(myList[i] > myList[1]):
            # sum += 1
            newList.append(myList[i])            
    print(len(newList))
    return(newList)
x = valuesGreaterThan2nd([3,2,3,4])
print(x)
#5
# def sizeAndVal(a,b):
#     myList = []
#     for i in range(b):
#         # if(len(myList) < b):
#         myList.append(a)
#     return myList
# x = sizeAndVal(6,3)
# print(x)