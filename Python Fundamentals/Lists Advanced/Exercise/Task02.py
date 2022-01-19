old_version = input().split(".")

n1 = int(old_version[0])
n2 = int(old_version[1])
n3 = int(old_version[2])

n3 += 1
if n3 > 9:
    n3 = 0
    n2 += 1

    if n2 > 9:
        n2 = 0
        n1 += 1

print("{}.{}.{}".format(n1, n2, n3))