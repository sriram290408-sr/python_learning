def factorial(n):
    if n == 0:
        return "Invalid"
    elif n == 1:
        return 1
    elif n > 1:
        return n*factorial(n-1)

factorial(5)

def bin_se(arr,y):
    mid = len(arr)//2
    if mid > y:
        while mid < len(arr)-1:
            start = arr[mid]
            if start == y:
                return "True"
            else:
                mid += 1
    elif mid < y:
        while 0 < mid:
            start = arr[mid]
            if start == y:
                return "True"
            else:
                mid += 1
    else:
        return "False"
        
bin_se([18,24,27,32,46,80,97],80)