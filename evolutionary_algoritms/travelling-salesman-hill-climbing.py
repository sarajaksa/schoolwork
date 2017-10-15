import random
import math
import matplotlib.pyplot as plt

class TravellingSalesman():

    def __init__(self, number_of_cities=5, biggest_value=10):
        self.start_finish = (0,0)
        self.cities = [(random.uniform(0, biggest_value), random.uniform(0, biggest_value)) for i in range(number_of_cities - 1)]
        self.number_of_cities = number_of_cities
        self.smallest_length = math.inf
        self.all_numbers = []
        
    def path_length(self, cities):
        path = 0
        pair_of_cities = zip([self.start_finish] + cities, cities + [self.start_finish])
        for city1, city2 in pair_of_cities:
            path += math.sqrt(abs(city1[0] - city2[0])**2 + abs(city1[1] - city2[1])**2)
        if path <= self.smallest_length:
            self.smallest_length = path
            self.cities = cities
        return path
        
    def mutation(self, cities, number_fo_mutations=1):
        for i in range(0, number_fo_mutations):
            cities.append(cities.pop(random.randint(0,self.number_of_cities - 2)))
        self.path_length(cities)
        
    def number_of_steps(self, step_number=1000, number_of_mutations=1):
        for i in range(step_number):
            self.mutation(self.cities, number_of_mutations)
            self.all_numbers.append(self.smallest_length)
            
        plt.plot(self.all_numbers)
        plt.show()
        

        
a = TravellingSalesman(10)
a.number_of_steps(1000, 3)
