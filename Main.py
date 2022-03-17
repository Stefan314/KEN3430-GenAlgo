import networkx as nx

from GGA import GGA
from GenomeTypes.IntString import IntString
from Problem.TSP import TSP
from Selection.RWS import RWS
from Selection.RandomSelection import RandomSelection


def main_tsp():
    # Change these to whatever is best for your problem
    pop_sz = 2000
    max_gens = 100
    pr_co = 0.6
    pr_mt = 0.15
    graph = tsp_graph()
    problem = TSP(start_node=0, graph=graph)

    # This should be the longest possible route
    length = sum(range(len(graph.nodes))) + len(graph.nodes) - 1
    base_gen = IntString(length=length, max_co=length - 1, max_int=3)
    sel_type = RandomSelection()

    gga = GGA(pop_sz, max_gens, pr_co, pr_mt, base_gen, sel_type, problem)
    best_ind = gga.run()
    # Let the best individual do something. Like running your problem and printing out the solution to your problem
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


def main_knap():
    # Change these to whatever is best for your problem
    pop_sz = 2000
    max_gens = 100
    pr_co = 0.6
    pr_mt = 0.15
    graph = tsp_graph()
    problem = TSP(start_node=0, graph=graph)

    no_of_nodes = len(graph.nodes)
    # This should be the longest possible route
    length = no_of_nodes**sum(range(no_of_nodes))
    base_gen = IntString(length=length, max_co=length - 1, max_int=3)
    sel_type = RWS(temp=1.0)

    gga = GGA(pop_sz, max_gens, pr_co, pr_mt, base_gen, sel_type, problem)
    best_ind = gga.run()
    # Let the best individual do something. Like running your problem and printing out the solution to your problem
    print(best_ind)


if __name__ == '__main__':
    main_tsp()
