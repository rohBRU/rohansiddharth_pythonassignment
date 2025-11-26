def alternate_reverse(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        if i % 2 == 1:  # reverse every 2nd word
            result.append(words[i][::-1])
        else:
            result.append(words[i])

    return " ".join(result)

# Example
sentence = "Python is an amazing programming language"
print(alternate_reverse(sentence))
