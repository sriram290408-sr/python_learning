#sum - 1
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

#sum - 2
sample = "HelloWorld"
new = sample.lower()
count = 0
vow = "aeiou"

for i in new:
    if i in vow:
        count += 1
print(count)

#sum - 3
def reverse(word):
    new = word.split(" ")
    result = ""
    for i in new:
        result += str(i[::-1]) + " "
    print(result)
#Test Cases:
reverse("Coding is fun")
reverse("Python is an programming Language")

#sum - 4
def palindrome(s):
    new_s = ""
    for i in range(len(s)-1,-1,-1):
        new_s += s[i]
    if s == new_s:
        print("Yes")
    else:
        print("No")
#Test Cases:
palindrome("madam")
palindrome("sky")
palindrome("noon")

#sum - 5
def duplicate(samp):
    result = ""
    for i in samp:
        if i not in result:
            result += i
    print(result)
#Test Cases:
duplicate("programming")
duplicate("mississipi")
duplicate("sky")

#sum - 6
def frequency(c,sub):
    count = 0
    for i in c:
        if i == sub:
            count += 1
    print(count)
#Test Cases:
frequency("bannana","a")
frequency("missionary","s")
frequency("mississipi","i")

#sum - 7
def altrev(s):
    result = ""
    for i in s:
        if s[0] == i:
            result += s[-1]
        elif s[-1] == i:
            result += s[0]
        else:
            result += i
    print(result)

#Test Cases:
altrev("a1b$c")
altrev("v3d£n")

#sum - 8
def alt_rev(s):
    new = s.split(" ")
    result = ""
    for i in range(len(new)-1,-1,-1):
        result += new[i] + " "
    print(result)
#Test Cases:
alt_rev("I love coding")
alt_rev("Hello World")

#sum - 9
def alt_ev(alpha):
    new_a = alpha.split(" ")
    result = ""
    for i in range(0,len(new_a),+1):
        if (i+1)%2 == 0:
            result += str(new_a[i][::-1]) + " "
        else:
            result += new_a[i] + " "
    print(result)
#Test Cases:
alt_ev("Python is very powerful")
alt_ev("Hello World this is Windows")

#sum - 10
def alter_in(s,l,r):
    result = ""
    for i in range(0,len(s),+1):
        if s[l] == s[i]:
            result += s[r]
        elif s[r] == s[i]:
            result += s[l]
        else:
            result += s[i]
    print(result)
#Test Cases:
alter_in("abcdefg", 2, 5)
alter_in("wsfnaee", 1, 4)