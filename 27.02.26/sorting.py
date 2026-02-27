# 1 - Selection Sorting
num = [4,1,3,9,7]
for i in range(0,len(num),+1):
    temp = i
    for j in range(i+1,len(num),+1):
        if num[temp] > num[j]:
            num[temp], num[j] = num[j], num[temp]
print(num)

# 2 - Bubble Sorting
num = [13, 32, 26, 35, 10]
n = len(num)
for i in range(0, n-1, +1):
    for j in range(0, n-i-1, +1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(num)