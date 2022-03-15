from Individual import Individual
from Problem.ProblemName import ProblemName


class Problem:
    """
    Super class for all other problems. E.g., TSP and knapsack.
    """

    def __init__(self, name: ProblemName):
        """
        Inheriting classes should tell the super class what kind of problem they are.
        :param name: A string. This makes it easier to see what kind of problem is being handled.
        """
        self.name = name

    def fitness(self, ind: Individual):
        """
        Calculates the fitness of the given individual based on their genome.
        The fitness value of the individual will be changed.
        :param ind: The individual that we need to calculate the fitness for
        :return: None
        """
        pass
