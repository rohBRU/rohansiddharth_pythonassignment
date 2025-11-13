text = input("Enter a string: ").lower()
freq = {}
for ch in text:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1
for ch, count in freq.items():
    print(f"{ch} → {count}")
