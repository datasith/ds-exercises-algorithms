words = ["apple","array","enter","bored","gains"]

freq = {}
for word in words:
    for letter in set(word):
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1

print(freq)
