numbers = input().split(", ")


def palindrome(nums):
    for current_num in nums:
        palindrome_num = current_num[::-1]

        if current_num == palindrome_num:
            print("True")
        else:
            print(False)


palindrome(numbers)