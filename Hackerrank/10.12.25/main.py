# def getMoneySpent(keyboards, drives, b):
#       # Write your code here.
#     #start
#     new = []
#     new1 = []
#     for i in keyboards:
#         for j in drives:
#             sum_kd = i + j
#             new.append(sum_kd)
#     for k in new:
#         if k <= b:
#             new1.append(k)
#     if new1 == []:
#         print(-1)
#     else:
#         max_spend = max(new1)
#         print(max_spend)
#     #end

# getMoneySpent([40,50,60],[5,8,12],60)

# def catAndMouse(x, y, z):
#     #write your code here
#     #start
#     distancec1 = abs(x-z)
#     distancec2 = abs(y-z)
#     if distancec1 == distancec2:
#         print("Mouse C")
#     elif distancec1 > distancec2:
#         print("Cat B")
#     elif distancec2 > distancec1:
#         print("Cat A")
#     #end
# catAndMouse(1,2,3)
# catAndMouse(1,3,2)

num = [4,2,5,6,1,7]
#method-1
# result = []
# for i in num:
#     max_num = max(num)
#     result.append(max_num)
#     num.remove(max_num)
# print(result)

#method-2
for i in range(0,len(num),+1):
    for j in range(0,len(num),+1):
        if num[i] > num[j]:
            num[i] , num[j] = num[j] , num[i]
print(num)

#method-3
