import random

from typing import List

import Individual
from GenomeTypes.BitString import BitString
from GenomeTypes.Genome import Genome
from Problem.Problem import Problem
from Problem.TSP import TSP
from Selection.RandomSelection import RandomSelection
from Selection.Selection import Selection


class GGA:
    """
    Generic Genetic Algorithm for solving any problem
    """

    def __init__(self,
                 pop_size: int = 1000,
                 gen_count: int = 10,
                 prob_co: float = 0.5,
                 prob_mut: float = 0.1,
                 base_gen: Genome = None,
                 sel_type: Selection = None,
                 problem: Problem = None):
        """
        Constructor to set up some basic properties for the GA
        :param pop_size: Population size. Must be a positive integer.
        :param gen_count: Number of generations. Must be a positive integer.
        :param prob_co: Crossover probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%.
        :param prob_mut: Mutation probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%
        :param base_gen: Genotype representation. How the genome is being represented.
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

        if not base_gen:
            base_gen = BitString()
        self.base_gen = base_gen

        if not sel_type:
            sel_type = RandomSelection()
        self.sel_type = sel_type

        if not problem:
            problem = TSP()
        self.problem = problem

    def run(self) -> Individual.Individual:
        """
        Runs the GA to find the best individual
        :return: The individual with the highest fitness
        """
        # Initial population construction
        population = Individual.factory(self.base_gen, self.pop_size)

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

                children = [parent1, parent2]

                # If crossover doesn't happen, the children will be the same as the parents.
                if random.random() < self.prob_co:
                    # Crossover alters the genomes of the parents, so they can be turned into children.
                    parent1.genome.crossover(parent2.genome)

                for child in children:
                    # Mutation alters the genome of the child
                    child.genome.mutate(self.prob_mut)
                    population.append(child)
            self.fitness_full_pop(population)
        best_ind = population[0]
        for ind in population:
            if ind.fitness > best_ind.fitness:
                best_ind = ind
        return best_ind

    def fitness_full_pop(self, pop: List[Individual]):
        for ind in pop:
            self.problem.fitness(ind)
