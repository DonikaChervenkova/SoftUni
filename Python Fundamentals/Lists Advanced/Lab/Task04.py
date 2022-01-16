words = input().split(" ")
searched_palindrome = input()

palindromes = []

for current_word in words:
    reversed_word = current_word[::-1]

    if current_word == reversed_word:
        palindromes.append(current_word)

count_searched_palindrome = words.count(searched_palindrome)
print(palindromes)
print(f"Found palindrome {count_searched_palindrome} times")
