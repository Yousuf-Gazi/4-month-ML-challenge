word = "banana"
freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(f"word: {word}")
print(f"frequency: {freq}")
