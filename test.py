from pprint import pprint
items = [
    ("prod1", 10),
    ("prod2", 9),
    ("prod3", 12),
]

# prices = list(map(lambda x: x[1], items))
# print(prices)
filtered = list(filter(lambda x: x[1] >= 10, items))
# print(filtered)

sentence = "This is a common interview question"
char_frequence = {}
for char in sentence:
    if char in char_frequence:
        char_frequence[char] += 1
    else:
        char_frequence[char] = 1
sort_char = sorted(char_frequence.items(), key=lambda kv: kv[1], reverse=True)
print(sort_char[0])
