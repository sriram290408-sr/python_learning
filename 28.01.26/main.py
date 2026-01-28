def num(n):
    start = 0
    m = n
    while start < n:
        print((" "*start) + str(m) )
        m -= 1
        start += 1
        
#Test Cases:
num(1)
num(2)
num(3)
num(4)
num(5)
num(6)
num(7)