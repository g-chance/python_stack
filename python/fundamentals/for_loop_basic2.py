# #1
# def returnBig(myList):
#     for i in range(len(myList)):
#         if(myList[i] >= 0):
#             myList[i] = "big"
#     return myList
# x = returnBig([1,-2,3,4])
# print(x)
# #2
# def lastIsSumPos(myList):
#     sum = 0
#     for i in range(len(myList)):
#         if(myList[i] > 0):
#             sum += myList[i]
#         if(i == len(myList)-1):
#             myList[i] = sum
#     return myList
# x = lastIsSumPos([1,2,3,-4,5])
# print(x)
# #3
# def sumAll(myList):
#     sum = 0
#     for val in myList:
#         sum += val
#     return sum
# x = sumAll([5,6,5,2])
# #4
# def sumAll(myList):
#     sum = 0
#     for val in myList:
#         sum += val
#     return sum/len(myList)
# x = sumAll([7,6,6,3])
# print(x)
# #5
# def listLen(myList):
#     return len(myList)
# x = listLen([])
# print(x)
# #6
# def minVal(myList):
#     if(len(myList) < 0):
#         return False
#     min = myList[0]
#     for val in myList:
#         if val < min:
#             min = val
#     return min
# x = minVal([-3,5,1,-2,7])
# print(x)
# #7
# def maxVal(myList):
#     if(len(myList) < 0):
#         return False
#     max = myList[0]
#     for val in myList:
#         if val > max:
#             max = val
#     return max
# x = maxVal([-3,9,1,-2,7])
# print(x)
# #8
# def createDict(myList):
#     dict = {}
#     sum = 0
#     max = myList[0]
#     min = myList[0]
#     for val in myList:
#         sum += val
#         if val > max:
#             max = val
#         if val < min:
#             min = val
#     dict["sum"] = sum
#     dict["max"] = max
#     dict["min"] = min
#     dict["avg"] = sum/len(myList)
#     dict["length"] = len(myList)
#     return dict
# x = createDict([2,6,-3,4])
# print(x)
#9
def reverseList(myList):
    for i in range(len(myList)//2):
        print i
        temp = myList[i]
        myList[i] = myList[len(myList)-1-i]
        myList[len(myList)-1-i] = temp
    return myList
x = reverseList([4,2,4,3,4,5])
print(x)