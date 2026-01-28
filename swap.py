num = [4,2,5,6,1,7]
counti = 0
countj = 0
#method-2
for i in range(0,len(num)-1,+1):
    counti += 1
    for j in range(i+1):
        countj += 1
        if num[i] > num[j]:
            num[i] , num[j] = num[j] , num[i]
print(num, counti, countj)