def find_duplicates(words):
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    duplicates = {key: value for key, value in freq.items() if value > 1}
    return duplicates

# Example
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
print(find_duplicates(words))
