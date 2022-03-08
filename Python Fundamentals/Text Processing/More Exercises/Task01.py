n = int(input())

for _ in range(n):
    line = input()
    start_name = line.find("@") + 1
    end_name = line.find("|")
    name = line[start_name:end_name]
    start_age = line.find("#") + 1
    end_age = line.find("*")
    age = int(line[start_age:end_age])
    print(f"{name} is {age} years old.")

