def largest_word(sentence):
    words = sentence.split()
    longest = words[0]

    for w in words:
        if len(w) > len(longest):
            longest = w

    return longest

# Example
print(largest_word("Python programming is awesome"))