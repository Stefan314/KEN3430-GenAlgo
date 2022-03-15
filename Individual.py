from typing import List

from GenomeTypes.Genome import Genome


class Individual:
    """
    Individual of a population in the GA
    """

    def __init__(self, genome: Genome):
        self.genome = genome
        self.fitness = 0


def factory(base_gen: Genome, no_of_inds: int = 1) -> List[Individual]:
    """
    Creates new individuals with new genomes and a fitness set to 0
    :param base_gen: The base genome,
    this indicates what kind of genome is used to create new genomes for the new individuals.
    :param no_of_inds: Amount of new individuals to be created. 1 by default
    :return: A list of new individuals
    """
    new_inds = []
    for i in range(no_of_inds):
        new_inds.append(Individual(base_gen.new_genome()))
    return new_inds
