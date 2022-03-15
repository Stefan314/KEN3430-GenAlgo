from Individual import Individual
from Selection.SelectionType import SelectionType
import random

name = "Random"


class RandomSelection(SelectionType):
    def __init__(self):
        super().__init__(name)

    def select(self, pop: list[Individual]) -> Individual:
        # TODO: Implement
        # we take random Individuals, for a total of half the population. Repetitions are allowed.
        n = pop.len/2
        random.shuffle(pop)
        new_pop = list[Individual]
        for i in n:
            random_selection = random.randrange(len(pop))
            new_pop.append(pop[random_selection])

        pass
