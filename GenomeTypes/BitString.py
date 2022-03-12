from GenomeTypes.GenRep import GenRep
from GenomeTypes.Genome import Genome

gen_rep = GenRep.BITSTRING


class BitString(Genome):
    def __init__(self):
        super().__init__(gen_rep)

    def crossover(self, other_gen: "Genome"):
        # TODO: Implement
        pass

    def mutate(self):
        # TODO: Implement
        pass

    def new_genome(self) -> "Genome":
        # TODO: Implement
        pass
