def word_frequency(words):
    freq = {}
    for w in words:
        w = w.lower()
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

# Example
words = ["This", "is", "good", "is"]
print(word_frequency(words))
