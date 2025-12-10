num = [3, 4, 2, 1, 5]

i = 0
while i < len(num) - 1:
    if num[i] < num[i + 1]:   
        num[i], num[i + 1] = num[i + 1], num[i]
        i = 0                 
    else:
        i += 1
print(num)

def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    best = 0
    worst = 0
    
    for i in scores[1:]:       
        if i > highest:        
            best += 1
            highest = i
        elif i < lowest:       
            worst += 1
            lowest = i         
    
    return best, worst

print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))