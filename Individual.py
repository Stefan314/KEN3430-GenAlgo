from GenomeTypes.BitString import BitString
from GenomeTypes.GenRep import GenRep
from GenomeTypes.Genome import Genome


class Individual:
    """
    Individual of a population in the GA
    """

    def __init__(self, genome: Genome):
        self.genome = genome
        self.fitness = 0


def factory(gen_rep: GenRep) -> Individual:
    if gen_rep == GenRep.BITSTRING:
        genome = BitString()
    else:
        raise Exception("This Genome Representation is not available.")
    return Individual(genome)
