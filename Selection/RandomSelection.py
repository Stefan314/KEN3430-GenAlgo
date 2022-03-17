import random

from Selection.Selection import Selection
from Selection.SelectionType import SelectionType


class RandomSelection(Selection):
    def __init__(self):
        super().__init__(SelectionType.RWS)

    def select(self, pop):
        # we take random Individuals, Repetitions are allowed.
        n = len(pop)
        random.shuffle(pop)
        new_pop = []
        for i in range(n):
            random_selection = random.randrange(len(pop))
            new_pop.append(pop[random_selection])

        return new_pop
