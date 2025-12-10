def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    #start
    counta = []
    counto = []
    apple = 0
    orange = 0
    
    for i in apples:
        sum_a = a + i
        counta.append(sum_a)
    
    for j in oranges:
        sum_o = b + j
        counto.append(sum_o)
    
    for k in counta:
        if s <= k <= t:
            apple += 1
    
    for m in counto:               
        if s <= m <= t:            
            orange += 1
    
    print(apple)
    print(orange)
    #end  
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])

def sockMerchant(n, ar):
    # Write your code here
    #start
    uni = []
    result = 0
    for i in ar:
        if i not in uni:
            uni.append(i)
    for j in uni:
        count = 0
        for k in ar:
            if j == k:
                count += 1
        div = int(count/2)
        result += div
    return result
    #end
    
sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])