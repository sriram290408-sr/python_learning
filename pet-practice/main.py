# sum -2
def duplicate_remove(sent):
    sent = sent.lower()
    result = ""
    for i in sent:
        if i not in result :
            result += i
    print(result)

duplicate_remove("programming")
duplicate_remove("MISSIPI")

# sum -2
def long_word(s):
    words = s.split()
    longest = words[0]

    for w in words:
        if len(w) > len(longest):
            longest = w

    return longest
print(long_word("python programming is very intresting"))

# sum-3
def count_substring(main_string, sub_string): 
    count = 0
    count_j = -1
    for i in range(0,len(main_string),+1):
        k = 0
        k += i
        new = "" 
        for j in range(k,len(main_string),+1):
            count_j += 1
            if count_j < len(sub_string):
                new += main_string[j]
            elif len(new) == len(sub_string):
                if new in sub_string:
                    count += 1
                    count_j = 0
    print(count)
(count_substring("ababab", "aba"))

# sum-4
num = 548
count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)