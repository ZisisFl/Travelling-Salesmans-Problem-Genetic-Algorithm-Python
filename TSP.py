import random

population = []
routes_length = []
overwrite_flag = 0
population_size = 20  # max 120 combinations
mut_prob = 0.4
n_generations = 200


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
    if overwrite_flag == 0:
        for i in range(population_size):
            route_l = 0
            for j in range(1, 5):
                route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
            routes_length.append(route_l)
    else:
        for i in range(population_size):
            route_l = 0
            for j in range(1, 5):
                route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
            routes_length[i] = route_l


def create_population():
    for i in range(population_size):
        population.append(create_route())


def swap_mutation():
    picks = random.sample(range(0, 4), 2)
    temp = population[1][picks[0]]
    population[1][picks[0]] = population[1][picks[1]]
    population[1][picks[1]] = temp
    print(population[1])


create_population()
calc_route_length()
print(population)
print(routes_length)

swap_mutation()
overwrite_flag = 1
calc_route_length()
print(routes_length)










