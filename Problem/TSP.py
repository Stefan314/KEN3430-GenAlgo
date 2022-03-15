from Individual import Individual
from Problem.Problem import Problem
from Problem.ProblemName import ProblemName


class TSP(Problem):

    def __init__(self):
        super().__init__(ProblemName.TSP)

    def fitness(self, ind: Individual):
        # TODO: Implement
        pass
