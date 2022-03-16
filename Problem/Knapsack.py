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
        self.max_weight = 10
        self.item_values = [i for i in range(1, self.n + 1)]
        self.item_weights = [random.randint(1, self.n) for i in range(0, self.n)]

    def fitness(self, ind: Individual):
        fitness = 0
        total_weight = 0
        for i in range(self.n):
            fitness += self.item_values[i] * ind.genome[i]
            if ind.genome[i] == 1:
                total_weight += self.item_weights[i]
        if total_weight > self.max_weight:
            fitness = 0
        ind.fitness = fitness
