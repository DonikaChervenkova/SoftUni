all_fire_cells = input().split("#")
water = int(input())

effort = 0
total_fire = 0
cells_fire_down = []

for current_fire in all_fire_cells:
    current_fire = current_fire.split(" ")

    level_of_fire = current_fire[0]
    value = int(current_fire[2])

    if level_of_fire == "High":
        if 81 <= value <= 125:
            if water >= value:
                water -= value
                effort += (0.25 * value)
                total_fire += value
                cells_fire_down.append(value)

    elif level_of_fire == "Medium":
        if 51 <= value <= 80:
            if water >= value:
                water -= value
                effort += (0.25 * value)
                total_fire += value
                cells_fire_down.append(value)

    elif level_of_fire == "Low":
        if 1 <= value <= 50:
            if water >= value:
                water -= value
                effort += (0.25 * value)
                total_fire += value
                cells_fire_down.append(value)

print("Cells:")
for cell in cells_fire_down:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
