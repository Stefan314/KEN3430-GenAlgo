from Individual import Individual
from Problem.Problem import Problem


# TODO: Implement more selection types
class SelectionType:
    """
    Super class for all other selection types. E.g., TSP and knapsack.
    """

    def __init__(self, name: str):
        """
        Inheriting classes should tell the super class what kind of selection types they are.
        :param name: A string.
        This makes it easier to see what kind of selection types is being handled.
        """
        self.name = name

    def select(self, pop: list[Individual]) -> Individual:
        """
        Selects an individual, possibly based on their fitness.
        :param pop: The population where individuals can be picked from.
        :return: A selected individual
        """
        pass
