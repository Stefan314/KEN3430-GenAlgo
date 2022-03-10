from Genome import Genome


class Individual:
    """
    Individual of a population in the GA
    """

    def __init__(self, genome: Genome = None):
        if genome is None:
            # TODO: Implement proper initial genome
            genome = None
        self.genome = genome
        self.fitness = 0
