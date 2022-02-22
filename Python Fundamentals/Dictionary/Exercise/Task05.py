legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk_materials = {}
good_materials = {"shards": 0, "fragments": 0, "motes": 0}
got_a_legendary_item = False

line = input()
while got_a_legendary_item is False:
    line = line.split(" ")

    for idx in range(1, len(line), 2):
        current_material = line[idx].lower()
        current_quantity = int(line[idx - 1])

        # collect only good items
        if current_material in ("shards", "fragments", "motes"):
            good_materials[current_material] += current_quantity

            # check do we have 250 or more
            if good_materials[current_material] >= 250:
                print(f"{legendary_items[current_material]} obtained!")
                good_materials[current_material] -= 250
                got_a_legendary_item = True
                break
        if got_a_legendary_item:
            break

        # collect junk items
        if current_material not in ("shards", "fragments", "motes"):
            if current_material not in junk_materials:
                junk_materials[current_material] = current_quantity
            else:
                junk_materials[current_material] += current_quantity

    if got_a_legendary_item:
        break

    line = input()

if got_a_legendary_item:
    sorted_good_materials = dict(sorted(good_materials.items(), key=lambda x: (-x[1], x[0])))
    print('\n'.join(f"{k}: {v}" for k, v in sorted_good_materials.items()))

    sorted_junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
    print('\n'.join(f"{k}: {v}" for k, v in sorted_junk_materials.items()))