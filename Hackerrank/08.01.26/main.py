#sum-1
s = "SOSOOSOSOSOSOSSOSOSOSOSOSOS"
start = 0
count = 0
count1 = 0
new = ""
key = ["S","O","S"]
list1 = []
for i in range(len(s)):
    new += s[i]
    count += 1
    if count%3 == 0:
        list1.append(new)
        new = ""  
for j in list1:
    for k in range(0,len(j),+1):
        if j[k] != key[k]:
            count1 += 1
print(count1)