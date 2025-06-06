
sentence = input("Enter a sentence: ")

word_list = sentence.split()

word_count = {}

for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# without dictionary solution

unique_words = []
unique_words_count = []

for word in word_list:
    if word in unique_words:
        idx = unique_words.index(word)
        unique_words_count[idx] += 1
    else:
        unique_words.append(word)
        idx = len(unique_words) - 1
        unique_words_count.append(1)

i = 0
while i < len(unique_words):
    print(f'{unique_words[i]} : {unique_words_count[i]}')
    i += 1
