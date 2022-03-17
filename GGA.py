import random

import Individual
from GenomeTypes.BitString import BitString
from GenomeTypes.Genome import Genome
from Problem.Problem import Problem
from Problem.TSP import TSP
from Selection.RandomSelection import RandomSelection
from Selection.Selection import Selection


CONVERGENCE = 3


class GGA:
    """
    Generic Genetic Algorithm for solving any problem
    """

    def __init__(self,
                 pop_size: int = 1000,
                 max_generations: int = 10,
                 prob_co: float = 0.5,
                 prob_mut: float = 0.1,
                 base_gen: Genome = None,
                 sel_type: Selection = None,
                 problem: Problem = None):
        """
        Constructor to set up some basic properties for the GA
        :param pop_size: Population size. Must be a positive integer.
        :param max_generations: Number of generations. Must be a positive integer.
        :param prob_co: Crossover probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%.
        :param prob_mut: Mutation probability. Must be a float between 0 (inclusive) and 1 (inclusive),
        where 0 is 0% probability and 1 is 100%
        :param base_gen: Genotype representation. How the genome is being represented.
        :param sel_type: The selection type. How survival is determined.
        :param problem: The problem. Defines how fitness is calculated for each individual.
        """
        assert pop_size > 0
        assert max_generations > 0
        assert 0 <= prob_co <= 1
        assert 0 <= prob_mut <= 1

        self.pop_size = pop_size
        self.max_generations = max_generations
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
        no_change_counter = 0
        prev_best_ind_fitness = 0
        best_ind = None
        while counter < self.max_generations:
            counter += 1
            print("Generation: " + str(counter))
            # Fill mating pool
            mating_pool = self.sel_type.select(population)

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
                    try:
                        # Crossover alters the genomes of the parents, so they can be turned into children.
                        parent1.genome.crossover(parent2.genome)
                    except AttributeError:
                        print(population)
                        print(mating_pool)
                        print(children)
                        raise AttributeError("shucks")

                for child in children:
                    try:
                        # Mutation alters the genome of the child
                        child.genome.mutate(self.prob_mut)
                    except AttributeError:
                        print(population)
                        print(mating_pool)
                        print(children)
                        raise AttributeError("shucks")
                    if not child:
                        print("child: " + str(child))
                    population.append(child)
            self.fitness_full_pop(population)
            best_ind = population[0]
            for ind in population:
                if ind.fitness > best_ind.fitness:
                    best_ind = ind
            if prev_best_ind_fitness == best_ind.fitness:
                no_change_counter += 1
            else:
                no_change_counter = 0
            # If there were no changes in fitness for CONVERGENCE generations, then this problem has converged.
            if no_change_counter == CONVERGENCE:
                return best_ind
            prev_best_ind_fitness = best_ind.fitness
        return best_ind

    def fitness_full_pop(self, pop):
        for ind in pop:
            self.problem.fitness(ind)
