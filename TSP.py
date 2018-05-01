import random

population = []
routes_length = [0]*20
fitness = [0]*20
population_size = 20  # max 120 combinations
mutate_prop = 0.1
n_generations = 30


cities = ['A', 'B', 'C', 'D', 'E']
distances = [[0, 4, 4, 7, 3],
             [4, 0, 2, 3, 5],
             [4, 2, 0, 2, 3],
             [7, 3, 2, 0, 6],
             [3, 5, 3, 6, 0]]


def calc_distance(city1, city2):
    return distances[ord(city1)-65][ord(city2)-65]  # ord('A')=65


def create_route():
    shuffled = random.sample(cities, len(cities))
    return shuffled


def calc_route_length():
    for i in range(population_size):
        route_l = 0
        for j in range(1, len(cities)):
            route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
        routes_length[i] = route_l
        fitness[i] = 1 / routes_length[i]


def create_population():
    for i in range(population_size):
        population.append(create_route())


def swap_mutation(ind):
    picks = random.sample(range(len(cities)), 2)
    temp = population[ind][picks[0]]
    population[ind][picks[0]] = population[ind][picks[1]]
    population[ind][picks[1]] = temp
    #print("Mutated path: ", population[ind])


def partially_matched_crossover(ind1, ind2):
    size = len(cities)
    p1, p2 = [0] * size, [0] * size

    # Converts characters of a route to numbers
    for k in range(size):
        ind1[k] = ord(ind1[k]) - 65
        ind2[k] = ord(ind2[k]) - 65

    # Initialize the position of each indices in the individuals
    for k in range(size):
        p1[ind1[k]] = k
        p2[ind2[k]] = k
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

# Apply crossover between cx points
    for k in range(cxpoint1, cxpoint2):
    # Keep track of the selected values
        temp1 = ind1[k]
        temp2 = ind2[k]
    # Swap the matched value
        ind1[k], ind1[p1[temp2]] = temp2, temp1
        ind2[k], ind2[p2[temp1]] = temp1, temp2
    # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]
    # Restores individuals
    for k in range(size):
        ind1[k] = chr(ind1[k] + 65)
        ind2[k] = chr(ind2[k] + 65)
    return ind1, ind2


def roulette_wheel_selection():
    s = 0
    partial_s = 0
    ind = 0
    for m in range(population_size):
        s = s + fitness[m]
    rand = random.uniform(0, s)
    for m in range(population_size):
        if partial_s < rand:
            partial_s = partial_s + fitness[m]
            ind = ind + 1
    if ind == 20:
        ind = 19
    return ind


def find_fittest():
    key = 1000
    fittest = 0
    for i in range(20):
        if routes_length[i] < key:
            key = routes_length[i]
            fittest = i
    return fittest


def sort_alongside(routes_length, population):
    routes_length, population = (list(i) for i in zip(*sorted(zip(routes_length, population))))


create_population()
print("Population initialization:", "\n", population)
calc_route_length()
print("Population's paths length:", "\n", routes_length)
for i in range(10):
    parent1 = roulette_wheel_selection()
    parent2 = roulette_wheel_selection()
    population[i], population[i+1] = partially_matched_crossover(population[parent1], population[parent2])#population[1], population[1] old
    calc_route_length()
for i in range(20):
    rand = random.uniform(0, 1)
    if rand < mutate_prop:
        swap_mutation(i)
calc_route_length()
print("Best route for generation: ", population[find_fittest()], "\n" "Route length: ", routes_length[find_fittest()])
print(population)
print(routes_length)

#for j in range(n_generations):
#    for i in range(10):
#        parent1 = roulette_wheel_selection()
#        print(parent1)
#        parent2 = roulette_wheel_selection()
#        print(parent2)
#        population[i], population[i + 1] = partially_matched_crossover(population[parent1], population[
#            parent2])  # population[1], population[1] old
#        calc_route_length()
#    for i in range(20):
#        rand = random.uniform(0, 1)
#        if rand < mutate_prop:
#            swap_mutation(i)










