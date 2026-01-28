def prime_num(num):
    if num < 2:
        return "Not Prime"
    elif num == 2:
        return "Prime"
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Not a Prime"
        return "Prime"

print(prime_num(7))  
print(prime_num(6))  
print(prime_num(3))  
print(prime_num(2))  