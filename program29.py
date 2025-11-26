def vowel_count(word):
    return sum(c in "aeiouAEIOU" for c in word)

words = ["apple", "sky", "orange", "fly"]
words.sort(key=vowel_count)
print(words)
