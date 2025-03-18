
while True:
    line = input('Enter the line: ')
    if line == 'quit':
        break
    word = input('Enter the word: ')

    word_idx = line.find(word)

    if word_idx != -1:
        print(f"The word position is: {word_idx}")
    else:
        print("The word is not present in the line")
