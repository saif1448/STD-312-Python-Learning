from math import inf

def lyrics_to_frequencies(word_list):
    word_dict = {}
    for word in word_list:
        # word = word.lower().replace(',','')
        word_count = word_dict.get(word, 0)
        word_dict[word] = word_count + 1
    return word_dict

def get_highest_and_lowest_freq(word_dict):
    highest = -inf
    lowest = inf
    for word, count in word_dict.items():
        if count >= highest:
            highest = count
        if count <= lowest:
            lowest = count
    return (highest, lowest)

def get_word_list_by_freq(word_dict, freq):
    word_list = []
    for word, count in word_dict.items():
        if count == freq:
            word_list.append(word)
    return word_list

lyrics =  '''
 Love, love me do
 You know I love you
 I'll always be true
 So please, love me do
 Whoa, love me do
 Love, love me do
 You know I love you
 I'll always be true
 So please, love me do
 Whoa, love me do
 Someone to love
 Somebody new
 Someone to love
 Someone like you
 Love, love me do
 You know I love you
 I'll always be true
 So please, love me do
 Whoa, love me do
 Love, love me do
 You know I love you
 I'll always be true
 So please, love me do
 Whoa, love me do
 Yeah, love me do
 Whoa, oh, love me do
 '''

word_list = lyrics.split()
word_dict = lyrics_to_frequencies(word_list)

highest_freq, lowest_freq = get_highest_and_lowest_freq(word_dict)

highest_freq_words = get_word_list_by_freq(word_dict, highest_freq)
lowest_freq_words = get_word_list_by_freq(word_dict, lowest_freq)

print(word_dict)
print(highest_freq_words)
print(lowest_freq_words)