population = [int(i) for i in input().split(", ")]
min_wealth = int(input())

no_equal = False

for index, number in enumerate(population):
    if number < min_wealth:
        max_number = max(population)
        index_of_max_number = population.index(max_number)
        needed_wealth_to_poor = min_wealth - number
        extra_wealth_of_rich = max_number - min_wealth

        if extra_wealth_of_rich >= needed_wealth_to_poor:
            population[index] += needed_wealth_to_poor
            population[index_of_max_number] -= needed_wealth_to_poor

        else:
            no_equal = True
            print("No equal distribution possible")
            break

if not no_equal:
    print(population)