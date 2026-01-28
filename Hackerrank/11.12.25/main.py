def birthday(s, d, m):
    #writeyour code here
    #start
    ways = 0
    for i in range(0, len(s) - m + 1):
        result = 0
        for j in range(i, i + m):
            result += s[j]
        if result == d:
            ways += 1

    return ways
    #end

print(birthday([2,2,1,3,2],4,2))
print(birthday([5,2,2,1,5,3,2], 9, 3))
print(birthday([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1],18,7))