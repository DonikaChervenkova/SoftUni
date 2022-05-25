def fill_the_box(height, length, width, *numbers):
    numbers = list(numbers)
    box = height * length * width
    while True:
        number = numbers.pop(0)
        if number == "Finish":
            break
        box -= number
    if box > 0:
        return f"There is free space in the box. You could put {box} more cubes."
    elif box < 0:
        return f"No more free space! You have {abs(box)} more cubes."
