count_words = {}
text = input("Text: ")

words = text.split()
print(words)

for i in words:
    count_words[i] = count_words.get(i, 0) + 1

words = list(count_words)
words.sort()

max_length = max((len(word) for word in words))
for i in words:
    print("{:{}} : {}".format(i, max_length, count_words[i]))