words = input().split(", ")

for word in words:
    if 3 <= len(word) <= 16:
        if word.isalnum() or "-" in word or "_" in word:
            print(word)
