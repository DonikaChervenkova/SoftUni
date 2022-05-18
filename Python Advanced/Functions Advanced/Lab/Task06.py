def operate(symbol, *nums):
    result = None

    if symbol == '+':
        result = sum(nums)

    elif symbol == '-':
        result = nums[0]
        for num in nums[1:]:
            result -= num

    elif symbol == '*':
        result = 1
        for num in nums:
            result *= num

    elif symbol == '/':
        result = nums[0]
        for num in nums[1:]:
            result /= num

    return result
