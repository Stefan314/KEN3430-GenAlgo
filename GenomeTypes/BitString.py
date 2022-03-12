import random

from GenomeTypes.GenRep import GenRep
from GenomeTypes.Genome import Genome

gen_rep = GenRep.BITSTRING
prop_0 = 0.5


class BitString(Genome):

    # The possible crossover points (all indices of the bitstring plus one)
    possible_co_pts: list[int]

    def __init__(self, length: int = 10, max_co: int = 9):
        """
        Generates random bit string of the given length.
        :param length: Length of the bit string. Needs to be a positive integer.
        :param max_co: Amount of crossover points. Needs to be a positive integer lower than or equal to length.
        """
        assert 0 < length
        assert 0 < max_co <= length
        super().__init__(gen_rep)
        self.max_co = max_co
        self.bitstring = []
        self.possible_co_pts = []
        for i in range(length):
            self.bitstring.append(random.random() < prop_0)
            self.possible_co_pts.append(i)
        self.possible_co_pts.append(length)

    def crossover(self, other_gen: "BitString"):
        random.shuffle(self.possible_co_pts)
        co_pts = self.possible_co_pts[0:self.max_co]
        switch = False
        for i in range(len(self)):
            if i in co_pts:
                switch = not switch
            if switch:
                temp = self.bitstring[i]
                self.bitstring[i] = other_gen.bitstring[i]
                other_gen.bitstring[i] = temp

    def mutate(self, prob_mut: float):
        for i in range(len(self)):
            bit_bool = self.bitstring[i]
            mut = random.random() < prob_mut
            self.bitstring[i] = (bit_bool and not mut) or (not bit_bool and mut)

    def new_genome(self) -> "Genome":
        return self.__init__(len(self))

    def __len__(self):
        return len(self.bitstring)
