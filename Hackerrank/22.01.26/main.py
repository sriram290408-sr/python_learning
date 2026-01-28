s = "saveChangesInTheEditor"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 1
for i in range(0,len(s),+1):
    if s[i] in alpha:
        count += 1