def do_swap(nums, comm):
    idx_1 = int(comm[1])
    idx_2 = int(comm[2])
    nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]


def do_multiply(nums, comm):
    idx_1 = int(comm[1])
    idx_2 = int(comm[2])
    result = nums[idx_1] * nums[idx_2]
    nums[idx_1] = result


def do_decrease(nums):
    nums = [i - 1 for i in nums]
    return nums


numbers = [int(i) for i in input().split(" ")]

command = input()
while command != "end":
    command = command.split(" ")
    to_do = command[0]

    if to_do == "swap":
        do_swap(numbers, command)

    elif to_do == "multiply":
        do_multiply(numbers, command)

    elif to_do == "decrease":
        numbers = do_decrease(numbers)

    command = input()

print(", ".join([str(i) for i in numbers]))