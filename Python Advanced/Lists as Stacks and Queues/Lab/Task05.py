people = input().split()

n = int(input())
idx = n - 1
while len(people) > 1:
    if 0 <= idx < len(people):
        print(f"Removed {people.pop(idx)}")
        idx += n-1
    else:
        idx = idx - (idx // len(people)) * len(people)
        print(f"Removed {people.pop(idx)}")
        idx += n-1


print(f"Last is {''.join(people)}")

