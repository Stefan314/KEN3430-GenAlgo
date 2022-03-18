import random

import networkx as nx

from GGA import GGA

from Problem.Knapsack import Knapsack
from Problem.TSP import TSP
from Selection.RWS import RWS
from Selection.RandomSelection import RandomSelection


def main_tsp():
    # Change these to whatever is best for your problem
    pop_sz = 2000
    max_gens = 100
    pr_co = 0.6
    pr_mt = 0.15
    graph = tsp_random_graph()
    problem = TSP(start_node=0, graph=graph)

    # This should be the longest possible route
    sel_type = RandomSelection()

    gga = GGA(pop_sz, max_gens, pr_co, pr_mt, sel_type, problem)
    best_ind = gga.run()
    # Let the best individual do something. Like running your problem and printing out the solution to your problem
    print("Best individual:")
    print(best_ind)
    # Printing the solution
    problem.fitness(best_ind, True)


def tsp_graph():
    graph = nx.Graph()

    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(0, 1, weight=10)
    graph.add_edge(0, 2, weight=15)
    graph.add_edge(0, 3, weight=20)
    graph.add_edge(2, 1, weight=35)
    graph.add_edge(3, 1, weight=25)
    graph.add_edge(2, 3, weight=30)

    return graph


def tsp_random_graph():
    graph = nx.Graph()

    no_of_nodes = random.randint(4, 10)

    for i in range(no_of_nodes):
        graph.add_node(i)

    for i in range(len(graph.nodes)):
        for j in range(i + 1, len(graph.nodes)):
            random_weight = random.uniform(0, 30)
            graph.add_edge(i, j, weight=random_weight)

    return graph


def main_knap():
    # Change these to whatever is best for your problem
    pop_sz = 2000
    max_gens = 100
    pr_co = 0.6
    pr_mt = 0.15

    # This should be the longest possible route
    problem = Knapsack(15, 4)

    sel_type = RWS(temp=1.0)

    gga = GGA(pop_sz, max_gens, pr_co, pr_mt, sel_type, problem)
    best_ind = gga.run()
    # Let the best individual do something. Like running your problem and printing out the solution to your problem
    print(best_ind)


if __name__ == '__main__':
    # Change to main_knap() or main_tsp() depending on what you want to test
    # main_knap()
    main_tsp()
