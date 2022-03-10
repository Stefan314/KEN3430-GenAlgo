from GR.GenotypeRepresentation import GenotypeRepresentation
from Genome import Genome
from Individual import Individual

gen_rep_name = "Bit String"


class BitString(GenotypeRepresentation):

    def __init__(self):
        super().__init__(gen_rep_name)

    def crossover(self, parents: list[Individual], prob_co: float) -> list[Individual]:
        # TODO: Implement
        pass

    def mutate(self, genome: Genome, prob_mut: float) -> None:
        # TODO: Implement
        pass
