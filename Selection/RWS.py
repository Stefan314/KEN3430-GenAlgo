from typing import List

from Individual import Individual
from Selection.Selection import Selection
from Selection.SelectionType import SelectionType
import random

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

    def select(self, pop: List[Individual]) -> Individual:
        max_Fitness = sum([c.fitness for c in pop])
        required_chance = random.uniform(0, max_Fitness)
        current_chance = 0
        for Individual in pop:
            current_chance += Individual.fitness
            if current_chance > required_chance:
                return Individual