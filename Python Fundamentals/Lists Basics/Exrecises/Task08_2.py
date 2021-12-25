def check_water(current_water, current_value):
    if current_value <= current_water:
        return True


def put_out_fire(water_info, value_info, t_effort, fires_down):
    water_info -= value_info
    t_effort += (0.25 * value_info)
    fires_down.append(value_info)
    return water_info, t_effort, fires_down


cells = input().split("#")
water = int(input())

total_effort = 0
fires_out = []

for current_cell in cells:
    current_cell = current_cell.split(" = ")
    type_of_fire = current_cell[0]
    value = int(current_cell[1])

    if type_of_fire == "High":
        if 81 <= value <= 125:
            if check_water(water, value):
                water, total_effort, fires_out = put_out_fire(water, value, total_effort, fires_out)

    elif type_of_fire == "Medium":
        if 51 <= value <= 80:
            if check_water(water, value):
                water, total_effort, fires_out = put_out_fire(water, value, total_effort, fires_out)

    elif type_of_fire == "Low":
        if 1 <= value <= 50:
            if check_water(water, value):
                water, total_effort, fires_out = put_out_fire(water, value, total_effort, fires_out)

print("Cells:")
if fires_out:
    print("\n".join(" - " + str(fire) for fire in fires_out))
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(fires_out)}")