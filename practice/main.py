def add_num(num):
    result = []
    for i in range(0,len(num),+1):
        sum_n = 0
        new = str(num[i])
        for j in new:
           sum_n += int(j)
        result.append(sum_n)
    print(result)

add_num([148, 5072, 9999, 2025, 43019, 70008, 123456, 8901, 560, 111111])

def count_common_words(s1, s2):
    words1 = s1.lower().split()
    words2 = s2.lower().split()
    common = set(words1) & set(words2)
    return len(common)

print(count_common_words("hello world python code", "python is fun world"))
print(count_common_words("one two three", "four five six"))