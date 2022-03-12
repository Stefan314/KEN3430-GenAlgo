from Individual import Individual
from Selection.SelectionType import SelectionType

name = "Random"


class RWS(SelectionType):
    """
    Roulette wheel selection
    """

    def __init__(self, temp: float = 1.0):
        """
        :param temp: Temperature parameter for tuning of the roulette-wheel.
        Low temperature means more randomness, high temperature means more deterministic based on fitness value.
        """
        super().__init__(name)
        self.temp = temp

    def select(self, pop: list[Individual]) -> Individual:
        # TODO: Implement
        pass
