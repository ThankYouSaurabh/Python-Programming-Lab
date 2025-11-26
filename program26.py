from collections import Counter

s = "aaaaabbbbcccc"
n = 2

result = Counter(s).most_common(n)
print(result)
