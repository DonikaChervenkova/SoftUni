from collections import deque


def math_operations(*nums, **dict):
    final_dict = {
        'a': 0,
        's': 0,
        'd': 0,
        'm': 0
    }
    nums = list(nums)
    all_operations = deque([[k, v] for k, v in dict.items()])
    while nums:
        current_num = nums.pop(0)
        current_operation = all_operations[0]
        if current_operation[0] == 'a':
            result = current_operation[1] + current_num
            all_operations[0][1] = result
        elif current_operation[0] == 's':
            result = current_operation[1] - current_num
            all_operations[0][1] = result
        elif current_operation[0] == 'd':
            if current_num == 0:
                all_operations.append(all_operations.popleft())
                continue
            result = current_operation[1] / current_num
            all_operations[0][1] = result
        elif current_operation[0] == 'm':
            result = current_operation[1] * current_num
            all_operations[0][1] = result

        all_operations.append(all_operations.popleft())

    for sublist in all_operations:
        final_dict[sublist[0]] = sublist[1]

    return final_dict