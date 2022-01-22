electrons = int(input())

shells = []
count_shell = 1

while electrons > 0:
    current_shell = 2 * pow(count_shell, 2)

    if electrons >= current_shell:
        shells.append(current_shell)

        electrons -= current_shell
        count_shell += 1
    else:
        shells.append(electrons)
        electrons -= electrons

print(shells)


