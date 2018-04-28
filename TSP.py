import random

population = []
routes_length = [0]*20
fitness = [0]*20
population_size = 20  # max 120 combinations
mutate_prop = 0.1


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
        for j in range(1, 5):
            route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
        routes_length[i] = route_l
        fitness[i] = 1 / routes_length[i]


def create_population():
    for i in range(population_size):
        population.append(create_route())


def swap_mutation():
    picks = random.sample(range(0, 4), 2)
    temp = population[1][picks[0]]
    population[1][picks[0]] = population[1][picks[1]]
    population[1][picks[1]] = temp
    print(population[1])


def PartialyMatchedCrossover(ind1, ind2):
    size = 5
    p1, p2 = [0] * size, [0] * size

    # Converts characters of a route to numbers
    for i in range(size):
        ind1[i] = ord(ind1[i]) - 65
        ind2[i] = ord(ind2[i]) - 65
    # Initialize the position of each indices in the individuals
    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

# Apply crossover between cx points
    for i in range(cxpoint1, cxpoint2):
    # Keep track of the selected values
        temp1 = ind1[i]
        temp2 = ind2[i]
    # Swap the matched value
        ind1[i], ind1[p1[temp2]] = temp2, temp1
        ind2[i], ind2[p2[temp1]] = temp1, temp2
    # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]
    # Restores individuals
    for i in range(size):
        ind1[i] = chr(ind1[i] + 65)
        ind2[i] = chr(ind2[i] + 65)
    return ind1, ind2


def roulette_wheel_selection():
    s = 0
    partial_s = 0
    ind = 0
    for i in range(population_size):
        s = s + fitness[i]
    rand = random.uniform(0, s)
    for i in range(population_size):
        if partial_s < rand:
            partial_s = partial_s + fitness[i]
            ind = i
    print(ind)


create_population()
calc_route_length()
print(population)
print(routes_length)

PartialyMatchedCrossover(population[0], population[1])
calc_route_length()
print(population)
print(routes_length)

swap_mutation()
calc_route_length()
print(population)
print(routes_length)


routes_length, population = (list(i) for i in zip(*sorted(zip(routes_length, population))))
print(population)
print(routes_length)
print(fitness)
roulette_wheel_selection()












