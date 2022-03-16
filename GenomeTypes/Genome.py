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
        Should be overwritten by inheriting classes.
        :param other_gen: The other genome that will perform crossover with the current genome.
        :return: None
        """
        pass

    def mutate(self, prob_mut: float):
        """
        Performs mutation on the current genome. Will change the current genome.
        Should be overwritten by inheriting classes.
        :param prob_mut: Mutation probability. Is used to mutate each gene with this probability.
        Must be a float between 0 (inclusive) and 1 (inclusive), where 0 is 0% probability and 1 is 100%.
        :return: None
        """
        pass

    def new_genome(self) -> "Genome":
        """
        Creates a new genome based on the current genome.
        It will be similar attribute-wise, but the contents will be different.
        Should be overwritten by inheriting classes.
        :return: A new genome based on the current one.
        """
        pass

    def __getitem__(self, item):
        """
        If this class is inherited, and this method is implemented in this subclass than it will return sth useful
        """
        pass
