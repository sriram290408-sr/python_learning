#sum-1
def gradingStudents(grades):
    result = []
    
    for num in grades:
        new = 0
        remainder = num % 5
        
        if num < 38:
            result.append(num)
        
        elif remainder == 0:
            result.append(num)
        
        else:
            new = num + (5 - remainder)   
            new1 = new - num

            if new1 < 3:
                result.append(new)
            else:        
                result.append(num)
    
    return result

print(gradingStudents([73,67,38,33]))

#sum-2
def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 >= v1:
        return "NO"
    if x1 > x2 and v1 >= v2:
        return "NO"

    n = (x2 - x1) / (v1 - v2)
    p1 = x1 + (n * v1)
    p2 = x2 + (n * v2)
    if p1 == p2:
        return "YES"
    else:
        return "NO"


print(kangaroo(0,2,5,3))
print(kangaroo(0,3,4,2))