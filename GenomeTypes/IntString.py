import random

from GenomeTypes.BitString import crossover
from GenomeTypes.GenRep import GenRep
from GenomeTypes.Genome import Genome

gen_rep = GenRep.BITSTRING


class IntString(Genome):

    def __init__(self, length: int = 10, max_co: int = 9, max_int: int = 2):
        """
        Generates random bit string of the given length.
        :param length: Length of the bit string. Needs to be a positive integer.
        :param max_co: Amount of crossover points. Needs to be a positive integer lower than or equal to length.
        """
        assert 0 < length
        assert 0 < max_co <= length
        super().__init__(gen_rep)
        self.max_co = max_co
        self.max_int = max_int
        self.string = []
        self.possible_co_pts = []
        for i in range(length):
            self.string.append(random.randint(0, self.max_int))
            self.possible_co_pts.append(i)
        self.possible_co_pts.append(length)

    def crossover(self, other_gen: "IntString"):
        crossover(self, other_gen)

    def mutate(self, prob_mut: float):
        for i in range(len(self)):
            mut = random.random() < prob_mut
            if mut:
                self.string[i] = random.randrange(0, self.max_int)

    def new_genome(self) -> "Genome":
        return IntString(len(self), self.max_co, self.max_int)

    def __len__(self):
        return len(self.string)

    def __getitem__(self, item):
        return self.string[item]

    def __str__(self):
        return "IntString: " + str(self.string) + "\nMax Int: " + str(self.max_int) + \
               "\nMax Cross-over points: " + str(self.max_co)
