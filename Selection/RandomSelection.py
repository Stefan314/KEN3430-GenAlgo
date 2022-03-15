from typing import List

from Individual import Individual
from Selection.Selection import Selection
from Selection.SelectionType import SelectionType
import random


class RandomSelection(Selection):
    def __init__(self):
        super().__init__(SelectionType.RWS)

    def select(self, pop: list[Individual]) -> Individual:

        # we take random Individuals, for a total of half the population. Repetitions are allowed.
        # n = pop.len/2
        # random.shuffle(pop)
        # new_pop = list[Individual]
        # for i in n:
        #     random_selection = random.randrange(len(pop))
        #     new_pop.append(pop[random_selection])
        random_selection = random.randrange(len(pop))
        return pop[random_selection]
