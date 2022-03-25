def check_index(trgs, idx):
    if 0 <= idx < len(trgs):
        return True


def reduce_targets(shot_trg):
    global targets
    for i, num in enumerate(targets):
        if num != -1:
            if num > shot_trg:
                targets[i] -= shot_trg
            else:
                targets[i] += shot_trg


targets = [int(i) for i in input().split(" ")]

count_shots = 0
command = input()

while command != "End":
    index = int(command)
    if check_index(targets, index) and targets[index] != -1:
        shot_target = targets[index]
        targets[index] = -1
        count_shots += 1

        reduce_targets(shot_target)

    command = input()

targets = " ".join([str(i) for i in targets])
print(f"Shot targets: {count_shots} -> {targets}")