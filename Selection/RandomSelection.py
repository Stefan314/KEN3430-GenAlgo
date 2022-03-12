from Individual import Individual
from Selection.SelectionType import SelectionType

name = "Random"


class RandomSelection(SelectionType):
    def __init__(self):
        super().__init__(name)

    def select(self, pop: list[Individual]) -> Individual:
        # TODO: Implement
        pass
