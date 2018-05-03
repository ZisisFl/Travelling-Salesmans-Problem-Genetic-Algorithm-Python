Travelling Salesmans Problem Genetic Algorithm Python
=====================================================

Our problem isn't demanding in processing power because we have only 5 cities and it is really easy to calculate the length of all the possibly routes and then pick the best. So this is a toy example but the algorithm can be generalized by changing the variables(population_size and n_generartions) and the distance matrix. The number of diffrent paths is equal to the factorial of the number of the cities, in this case 5! = 120. It is pretty clear that as the number of cities increases the problem becomes more and more difficult and this is the reason that we choose a genetic algorithm to solve it.

This algorithm is based on the image below.

![ai asign](https://user-images.githubusercontent.com/15019941/39580720-74aa64ce-4ef2-11e8-8bb9-3d1cf3653a9a.jpg)

From this image results the distance matrix, but any distance matrix given to the algorithm can give us back a result.

The mutation method is swap mutation with probability 10% for every path in the population. Crossover method is PMX and it is considered as one of the best for this problem. Parents for the crossover are choosed with Fitness Proportionate Selection. We have selected Roulette Wheel Selection which is a way to give higher chance for best routes to be choosen as parents based on their fitness (1/route_length).

Useful links:  
https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm  
https://iccl.inf.tu-dresden.de/w/images/b/b7/GA_for_TSP.pdf
