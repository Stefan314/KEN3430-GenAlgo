import random

from GenomeTypes.GenRep import GenRep
from GenomeTypes.Genome import Genome

gen_rep = GenRep.BITSTRING
prop_0 = 0.5


class BitString(Genome):

    def __init__(self, length: int = 10, max_co: int = -1):
        """
        Generates random bit string of the given length.
        :param length: Length of the bit string. Needs to be a positive integer.
        :param max_co: Amount of crossover points. Needs to be a positive integer lower than or equal to length.
        If it's not, then it will be length - 1
        """
        assert 0 < length
        super().__init__(gen_rep)
        if not 0 < max_co <= length:
            max_co = length - 1
        self.max_co = max_co
        self.string = []
        self.possible_co_pts = []
        for i in range(length):
            self.string.append(random.random() < prop_0)
            self.possible_co_pts.append(i)
        self.possible_co_pts.append(length)

    def crossover(self, other_gen: "BitString"):
        crossover(self, other_gen)

    def mutate(self, prob_mut: float):
        for i in range(len(self)):
            bit_bool = self.string[i]
            mut = random.random() < prob_mut
            self.string[i] = (bit_bool and not mut) or (not bit_bool and mut)

    def new_genome(self) -> "Genome":
        return BitString(len(self), self.max_co)

    def __len__(self):
        return len(self.string)

    def __getitem__(self, item):
        return self.string[item]


def crossover(genome1, genome2):
    # Shuffles the possible crossover points. The first of these will be taken.
    # This ensures that the crossovers are random and that there are always enough crossovers.
    random.shuffle(genome1.possible_co_pts)
    co_pts = genome1.possible_co_pts[0:genome1.max_co]
    switch = False
    for i in range(len(genome1)):
        # If the index is in the used crossover points. Then crossover happens
        if i in co_pts:
            switch = not switch
        if switch:
            # When crossover happens, then the elements of the genomes will be switched
            temp = genome1.string[i]
            genome1.string[i] = genome2.string[i]
            genome2.string[i] = temp
