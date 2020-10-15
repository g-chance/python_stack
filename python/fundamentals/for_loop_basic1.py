# for num in range(151):
#     print(num)
# for num in range(5,1001,5):
#     print(num)
# for num in range(1,101,1):
#     if(num%10 == 0):
#         print("Coding Dojo")
#     elif(num%5 == 0):
#         print("Coding")
#     else:
#         print(num)
# sum = 0
# for num in range(1,500000,2):
#     sum += num
# print(sum)
# for num in range(2018,-1,-4):
#     print(num)
lowNum = -5
highNum = 8
mult = 4
for num in range(lowNum,highNum+1,1):
    if(num % mult) == 0:
        print(num)