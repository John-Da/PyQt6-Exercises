def count_words(words):
    lowerCase = words.lower()
    wordSplit = lowerCase.split()
    word_list = {}

    for word in wordSplit:
        if len(word) >= 3:
            if word in word_list:
                word_list[word] += 1
            else:
                word_list[word] = 1

    return word_list


sample_text1 = "The quick brown fox jumps over the lazy dog"
print(count_words(sample_text1))
sample_text2 = "If you believe in something and put it in your mind and heart, it can be realised. -Eliud Kipchoge"
print(count_words(sample_text2))
