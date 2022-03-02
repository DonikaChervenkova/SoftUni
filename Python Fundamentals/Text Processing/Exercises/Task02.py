both_strings = input().split(" ")
str1 = both_strings[0]
str2 = both_strings[1]
total_result = 0

if len(str1) == len(str2):
    total_result = sum([ord(letter_1) * ord(letter_2) for letter_1, letter_2 in zip(str1, str2)])
else:
    if len(str1) > len(str2):
        last_common_idx = len(str2)
        str1_common_part = str1[:last_common_idx]
        str1_rest_part = str1[last_common_idx:]
        result_1 = sum([ord(letter_1) * ord(letter_2) for letter_1, letter_2 in zip(str1_common_part, str2)])
        result_2 = sum([ord(letter) for letter in str1_rest_part])
        total_result = result_1 + result_2

    elif len(str2) > len(str1):
        last_common_idx = len(str1)
        str2_common_part = str2[:last_common_idx]
        str2_rest_part = str2[last_common_idx:]
        result_1 = sum([ord(letter_1) * ord(letter_2) for letter_1, letter_2 in zip(str1, str2_common_part)])
        result_2 = sum([ord(letter) for letter in str2_rest_part])
        total_result = result_1 + result_2

print(total_result)