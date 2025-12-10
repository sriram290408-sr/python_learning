def divisibleSumPairs(n, k, ar):
    #start
    count = 0
    for a in range(n):
        for b in range(n):
            if a < b:  
                add_ar = ar[a] + ar[b]
                if add_ar % k == 0:  
                    count += 1
    return count
    #end

print(divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2]))

def max_occuring(sent):
    new = []
    new1 = {}
    for i in sent:
        if i not in new and i != " ":
            new.append(i)
    for j in range(len(new)):
        count = 0
        for k in range(len(sent)):
            if new[j] == sent[k]:   
                count += 1
        new1[new[j]] = count
    max_value = max(new1, key=new1.get)
    print(max_value)
max_occuring("free bies")
max_occuring("persona")