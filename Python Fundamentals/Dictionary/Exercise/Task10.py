companies_info = {}
command = input()

# collect all info
while command != "End":
    information = command.split(" -> ")
    name = information[0]
    employee_id = information[1]

    companies_info.setdefault(name, []).append(employee_id)

    command = input()

#  remove employees with the same id
for k, v in companies_info.items():
    new_v = sorted(set(v), key=v.index)
    companies_info[k] = new_v

# sort
sorted_companies_info = dict(sorted(companies_info.items(), key=lambda x: x[0]))

for name, values in sorted_companies_info.items():
    print(name)
    print('\n'.join([f"-- {id}" for id in values]))