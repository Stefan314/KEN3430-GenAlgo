from typing import List

from Individual import Individual
from Selection.Selection import Selection
from Selection.SelectionType import SelectionType


class RandomSelection(Selection):
    def __init__(self):
        super().__init__(SelectionType.RWS)

    def select(self, pop: List[Individual]) -> Individual:
        # TODO: Implement
        pass
