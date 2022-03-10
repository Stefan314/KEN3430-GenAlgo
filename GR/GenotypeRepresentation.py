from Genome import Genome
from Individual import Individual


# TODO: Add more genotype reps
class GenotypeRepresentation:
    """
    Super class for all other genotype representations. E.g., a string of bits.
    """

    def __init__(self, gen_rep_name: str):
        """
        Inheriting classes should tell the super class what kind of genotype representation they are.
        :param gen_rep_name: A string.
        This makes it easier to see what kind of genotype representation is being handled.
        """
        self.gen_rep_name = gen_rep_name

    def crossover(self, parents: list[Individual], prob_co: float) -> list[Individual]:
        """
        Performs crossover on the parents if crossover happens (according to the crossover probability).
        This results in children.
        :param parents: Two individuals
        :param prob_co: A crossover probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%.
        :return: Two children (individuals)
        """
        pass

    def mutate(self, genome: Genome, prob_mut: float) -> None:
        """
        Mutates the genome according to a mutation probability. Alters the genome.
        :param genome: The genome of an individual
        :param prob_mut: A mutation probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%.
        :return: None
        """
        pass
