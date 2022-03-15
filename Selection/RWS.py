from typing import List

from Individual import Individual
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

    def select(self, pop: List[Individual]) -> Individual:
        # TODO: Implement
        pass
