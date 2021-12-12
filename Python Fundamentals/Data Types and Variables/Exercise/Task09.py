n = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for current_snowball in range(1, n + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > max_value:
        max_value = value
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")