def fibno(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibno(n-1) + fibno(n-2)
    
print(fibno(10))