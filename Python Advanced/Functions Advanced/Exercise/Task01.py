def my_function(numbers):
    result = []
    negative_nums = [num for num in numbers if num < 0]
    positive_nums = [num for num in numbers if num > 0]
    result.append(sum(negative_nums))
    result.append(sum(positive_nums))
    if abs(sum(negative_nums)) > abs(sum(positive_nums)):
        result.append("The negatives are stronger than the positives")
    elif abs(sum(negative_nums)) < abs(sum(positive_nums)):
        result.append("The positives are stronger than the negatives")

    return '\n'.join([str(i) for i in result])





print(my_function([int(i) for i in input().split()]))