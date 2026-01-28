#sum -1
word = "is this is an island"
sub = "is"
count = 0
for i in range(0,len(word)-1,+1):
    if word[i] == sub[0]:
        if word[i+1] == sub[1]:
            count += 1 
print(count)

#sum -2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new = []
for i in matrix:
    for j in i:
        new.append(j)
min_mat = min(new)
max_mat = max(new)
print(min_mat, max_mat)

#sum -3
word = "is this iS an island"
sub = "is"
word1 = word.lower()
count = 0
for i in range(0,len(word1)-1,+1):
    if word1[i] == sub[0]:
        if word[i-1] == " " or word1[i+2] == " ":
            if word1[i+1] == sub[1]:
                count += 1
print(count)

