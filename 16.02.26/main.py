def binarysearch(arr,x):
    low = 0
    high = len(arr)
    start = 0
    while start < len(arr)//2:
        mid = (low + high)//2
        low = mid
        if x > arr[mid]:
            start += 1
        elif x < arr[mid]:
            start += 1
            high = mid
            low = 0
        elif x == arr[mid]:
            return True
    return False
    
print(binarysearch([5,8,17,29,32,50,67,98], 1))
print(binarysearch([5,8,17,29,32,50,67,98], 17))
print(binarysearch([5,8,17,29,32,50,67,98], 32))
print(binarysearch([5,8,17,29,32,50,67,98], 99))