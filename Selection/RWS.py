import random

from Selection.Selection import Selection
from Selection.SelectionType import SelectionType


class RWS(Selection):
    """
    Roulette wheel selection
    """

    def __init__(self, temp: float = 1.0):
        """
        :param temp: Temperature parameter for tuning of the roulette-wheel.
        Low temperature means more randomness, high temperature means more deterministic based on fitness value.
        """
        super().__init__(SelectionType.RWS)
        self.temp = temp

    def select(self, pop):
        # Sort the population based on fitness
        max_fitness = sum([c.fitness for c in pop])
        new_pop = []
        print(max_fitness)
        for i in range(len(pop)):
            required_chance = random.uniform(0, max_fitness)
            current_chance = 0
            for individual in pop:
                current_chance += individual.fitness
                if current_chance >= required_chance:
                    new_pop.append(individual)
                    break
        return new_pop
