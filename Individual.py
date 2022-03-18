from GenomeTypes.Genome import Genome


class Individual:
    """
    Individual of a population in the GA
    """

    def __init__(self, genome: Genome):
        self.genome = genome
        self.fitness = 0.0

    def __str__(self):
        return "Genome:\n" + str(self.genome) + "\nFitness = " + str(self.fitness)
