all_heroes = {}

n = int(input())
max_hp = 100
max_mp = 200

for _ in range(n):
    info = input().split(" ")
    name = info[0]
    hp = int(info[1])
    mp = int(info[2])

    # collect info in dict
    if name not in all_heroes:
        all_heroes[name] = {}
        all_heroes[name]["hit points"] = hp
        all_heroes[name]["mana points"] = mp

# changes
command = input()
while command != "End":
    command = command.split(" - ")
    to_do = command[0]
    name = command[1]

    if to_do == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if mp_needed <= all_heroes[name]["mana points"]:
            all_heroes[name]["mana points"] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {all_heroes[name]['mana points']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif to_do == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        all_heroes[name]["hit points"] -= damage
        if all_heroes[name]["hit points"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {all_heroes[name]['hit points']} HP left!")
        else:
            del all_heroes[name]
            print(f"{name} has been killed by {attacker}!")

    elif to_do == "Recharge":
        amount = int(command[2])
        current_mp = all_heroes[name]["mana points"]
        used_amount_to_recover = min(amount, (max_mp - current_mp))
        all_heroes[name]["mana points"] += used_amount_to_recover
        print(f"{name} recharged for {used_amount_to_recover} MP!")

    elif to_do == "Heal":
        amount = int(command[2])
        current_hp = all_heroes[name]["hit points"]
        used_amount_to_recover = min(amount, (max_hp - current_hp))
        all_heroes[name]["hit points"] += used_amount_to_recover
        print(f"{name} healed for {used_amount_to_recover} HP!")

    command = input()

# sort
sorted_all_heroes = dict(sorted(all_heroes.items(),key=lambda kvp: (-kvp[1]['hit points'], kvp[0])))

for name in sorted_all_heroes:
    print(f"""{name}
  HP: {sorted_all_heroes[name]['hit points']}
  MP: {sorted_all_heroes[name]['mana points']}""")


