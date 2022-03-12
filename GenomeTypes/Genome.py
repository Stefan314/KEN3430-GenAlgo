from GenomeTypes.GenRep import GenRep


class Genome:
    """
    Super class of all genotype representations. The genome of an individual
    """

    def __init__(self, gen_rep: GenRep):
        """
        :param gen_rep: The genome representation
        """
        self.gr = gen_rep

    def crossover(self, other_gen: "Genome"):
        """
        Performs crossover on the current and the other genome. Will change both genomes.
        :param other_gen: The other genome that will perform crossover with the current genome.
        :return: None
        """
        pass

    def mutate(self):
        """
        Performs mutation on the current genome. Will change the current genome
        :return: None
        """
        pass
