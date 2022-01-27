text = input()

result_string = []
digits = [int(i) for i in text if i.isdigit()]
non_digits = [i for i in text if not i.isdigit()]
take_list = [num for idx, num in enumerate(digits) if idx % 2 == 0]
skip_list = [num for idx, num in enumerate(digits) if idx % 2 != 0]

take_skip_list = list(zip(take_list, skip_list))

start = 0
end = 0

for step in take_skip_list:
    take = step[0]
    skip = step[1]

    if step[0] != 0:
        end += take
        result_string += non_digits[start: end]
        start += take

    if skip != 0:
        end = start + skip
        start += skip

print("".join(result_string))



