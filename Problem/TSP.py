import networkx as nx

from Individual import Individual
from Problem.Problem import Problem
from Problem.ProblemName import ProblemName


class TSP(Problem):

    def __init__(self, graph: nx.Graph = None, start_node: int = None):
        super().__init__(ProblemName.TSP)
        self.graph = graph
        if not start_node:
            start_node = 0
        self.start_node = start_node

    def fitness(self, ind: Individual):
        # If the fitness is not 0, then this individual already had its fitness being calculated
        if ind.fitness != 0:
            return
        current_node = self.start_node
        visited_nodes = [current_node]
        path_length = 0
        # Loop over genome
        # End if all genes have been read or if all nodes have been visited
        for i in range(len(ind.genome)):
            # Using each gene choose next node
            next_node = ind.genome[i]
            # Check if there is an edge between current and next node.
            if self.graph.has_edge(current_node, next_node):
                # If there is, the weight of the edge will be added to the path length
                path_length += self.graph.get_edge_data(current_node, next_node)["weight"]
                # then current node will be the next node
                current_node = next_node
            else:
                # If there isn't, stop the method.
                break
            # If next node is not yet in the visited nodes, add it
            if next_node not in visited_nodes:
                visited_nodes.append(next_node)
            # Check if all nodes have been visited
            if len(visited_nodes) == len(self.graph.nodes):
                # Assign correct fitness to individual based on the path length.
                # Shorter path length means higher fitness.
                # So a 1/x formula is used, since path length shouldn't be negative.
                ind.fitness = 1 / path_length
                break
