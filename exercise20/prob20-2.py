sentence = "The quick brown fox jumps over the lazy dog"
long_words = list(filter((lambda x: x if len(x) > 3 else ''), sentence.split()))
print("Words with more than 3 characters:", long_words)