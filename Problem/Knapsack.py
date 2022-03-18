from GenomeTypes.BitString import BitString
from Individual import Individual
from Problem.Problem import Problem
from Problem.ProblemName import ProblemName
import random


class Knapsack(Problem):

    def __init__(self, genome):
        super().__init__(ProblemName.KNAPSACK)
        assert isinstance(genome, BitString)
        self.n = len(genome)

        #self.item_values = [1, 3, 5, 4, 2]
        #self.item_weights = [0.1, 10, 1, 2, 0.5]
        self.item_values = [i for i in range(1, self.n + 1)]
        self.item_weights = [random.randint(1, self.n) for i in range(0, self.n)]
        self.m = sum(self.item_weights)
        print(self.m)
        self.max_weight = random.randint(1,self.m)
        print(self.max_weight)
        print(self.item_values)
        print(self.item_weights)

    def fitness(self, ind: Individual, print_sol: bool = False):
        fitness = 0
        total_weight = 0

        for i in range(self.n):
            fitness += self.item_values[i] * ind.genome[i]
            if ind.genome[i] == 1:
                total_weight += self.item_weights[i]
        if total_weight > self.max_weight:
            fitness = 0

        ind.fitness = fitness