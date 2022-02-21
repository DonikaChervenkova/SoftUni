country_names = input().split(", ")
capitals = input().split(", ")

dictionary = dict(zip(country_names, capitals))
print("\n".join(f'{k} -> {v}' for k, v in dictionary.items()))