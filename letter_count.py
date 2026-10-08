word = input("Enter word: ")
letter = input("Enter letter: ")
count = 0

for ch in word:
    if ch == letter:
        count += 1

print(count) 