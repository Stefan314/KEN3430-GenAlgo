import random

from GR.BitString import BitString
from GR.GenotypeRepresentation import GenotypeRepresentation
from Individual import Individual
from Problem.Problem import Problem
from Problem.TSP import TSP
from Selection.RandomSelection import RandomSelection
from Selection.SelectionType import SelectionType


class GGA:
    """
    Generic Genetic Algorithm for solving any problem
    """

    def __init__(self, pop_size: int = 1000, gen_count: int = 10,
                 prob_co: float = 0.5, prob_mut: float = 0.1,
                 gen_rep: GenotypeRepresentation = None,
                 sel_type: SelectionType = None,
                 problem: Problem = None):
        """
        Constructor to set up some basic properties for the GA
        :param pop_size: Population size. Must be a positive integer.
        :param gen_count: Number of generations. Must be a positive integer.
        :param prob_co: Crossover probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%.
        :param prob_mut: Mutation probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%
        :param gen_rep: Genotype representation. How the genome is being represented.
        :param sel_type: The selection type. How survival is determined.
        :param problem: The problem. Defines how fitness is calculated for each individual.
        """
        assert pop_size > 0
        assert gen_count > 0
        assert 0 <= prob_co <= 1
        assert 0 <= prob_mut <= 1

        self.pop_size = pop_size
        self.gen_count = gen_count
        self.prob_co = prob_co
        self.prob_mut = prob_mut

        if gen_rep is None:
            gen_rep = BitString()
        self.gen_rep = gen_rep

        if sel_type is None:
            sel_type = RandomSelection()
        self.sel_type = sel_type

        if problem is None:
            problem = TSP()
        self.problem = problem

    def run(self) -> Individual:
        """
        Runs the GA to find the best individual
        :return: The individual with the highest fitness
        """
        # Initial population construction
        population = []
        for i in range(self.pop_size):
            population.append(Individual())

        self.fitness_full_pop(population)

        # Main GA
        counter = 0
        while counter < self.gen_count:
            # Fill mating pool
            mating_pool = []
            while len(mating_pool) != len(population):
                ind = self.sel_type.select(population)
                mating_pool.append(ind)

            # Generate new population from mating pool
            population = []
            while len(mating_pool) != 0:
                # Select random individuals from mating pool and remove them from the pool
                parent1 = mating_pool[random.randrange(0, len(mating_pool))]
                mating_pool.remove(parent1)
                parent2 = mating_pool[random.randrange(0, len(mating_pool))]
                mating_pool.remove(parent2)

                parents = [parent1, parent2]

                # If crossover doesn't happen, the children will be the same as the parents.
                children = self.gen_rep.crossover(parents, self.prob_co)

                for child in children:
                    self.gen_rep.mutate(child.genome, self.prob_mut)
                    population.append(child)
            self.fitness_full_pop(population)
        best_ind = population[0]
        for ind in population:
            if ind.fitness > best_ind.fitness:
                best_ind = ind
        return best_ind

    def fitness_full_pop(self, pop: list[Individual]):
        for ind in pop:
            self.problem.fitness(ind)
