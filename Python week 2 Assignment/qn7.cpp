def to_title_case(sentence):
    words = sentence.split()
    title_words = [w.capitalize() for w in words]
    return " ".join(title_words)

# Example
print(to_title_case("hello world from python"))