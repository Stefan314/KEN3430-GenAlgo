from Individual import Individual
from Problem.Problem import Problem
from Problem.ProblemName import ProblemName
import random

class Knapsack(Problem):

    def __init__(self,Genome):
        super().__init__(ProblemName.KNAPSACK)
        n = len(Genome)
        max_weight = 10
        item_values = [i for i in range(1, n+1)]
        item_weights = [random.randint(1, n) for i in range(0, n)]

    def fitness(self, ind: Individual, max_weight, item_weights, item_values):
        fitness = 0
        total_weight = 0
        for i in range(self.n):
            fitness += self.item_values[i] * self.genome[i]
            if self.genome[i] == 1:
                total_weight += self.item_weights[i]
        if total_weight > max_weight:
            fitness = 0
        self.fitness = fitness