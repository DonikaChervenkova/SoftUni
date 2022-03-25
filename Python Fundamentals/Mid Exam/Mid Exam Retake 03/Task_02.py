targets = [int(i) for i in input().split(" ")]

count_shots = 0
command = input()

while command != "End":
    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        count_shots += 1
        shot_target = targets[index]
        targets[index] = -1
        for i, target in enumerate(targets):
            if target != -1:
                if target > shot_target:
                    targets[i] -= shot_target
                else:
                    targets[i] += shot_target

    command = input()


targets = " ".join([str(i) for i in targets])
print(f"Shot targets: {count_shots} -> {targets}")

