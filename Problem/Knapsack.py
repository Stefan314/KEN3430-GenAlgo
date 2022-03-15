from Individual import Individual
from Problem.Problem import Problem
from Problem.ProblemName import ProblemName


class Knapsack(Problem):

    def __init__(self):
        super().__init__(ProblemName.KNAPSACK)

    def fitness(self, ind: Individual):
        fitness = 0
        total_weight = 0
        for i in range(self.n):
            fitness += self.item_values[i] * self.genome[i]
            if self.genome[i] == 1:
                total_weight += self.item_weights[i]
        if total_weight > max_weight:
            fitness = 0
        self.fitness = fitness