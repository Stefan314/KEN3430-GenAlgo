import networkx as nx

from GenomeTypes.IntString import IntString
from Individual import Individual
from Problem.Problem import Problem
from Problem.ProblemName import ProblemName


class TSP(Problem):

    def __init__(self, graph: nx.Graph = None, start_node: int = 0, max_co: int = 1):
        """
        :param graph: Represents the traveling salesperson problem. Edges have weights.
        :param start_node: The preferred starting node
        :param max_co: Maximum of crossover points.
        Needs to be a positive integer lower than or equal to
        sum(range(len(no_of_nodes_in_graph))) + len(no_of_nodes_in_graph) - 1
        """
        super().__init__(ProblemName.TSP)
        length = sum(range(len(graph.nodes))) + len(graph.nodes) - 1
        assert 0 < max_co <= length
        self.graph = graph
        self.start_node = start_node
        self.max_co = max_co

    def fitness(self, ind: Individual, print_sol: bool = False):
        current_node = self.start_node
        visited_nodes = [current_node]
        path_length = 0
        ind.fitness = 0
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
            if len(visited_nodes) == len(self.graph.nodes) and current_node == self.start_node:
                # Assign correct fitness to individual based on the path length.
                # Shorter path length means higher fitness.
                # So a 1/x formula is used, since path length shouldn't be negative.
                ind.fitness = 1 / path_length
                break
        if print_sol:
            if ind.fitness != 0:
                # Printing the path
                sol = "Solution:\n"
                for i in range(1, len(visited_nodes)):
                    prev_node = visited_nodes[i - 1]
                    node = visited_nodes[i]
                    edge_weight = self.graph.get_edge_data(prev_node, node)["weight"]
                    sol += str(prev_node) + " -> " + str(node) + " Weight: " + str(edge_weight) + "\n"

                prev_node = visited_nodes[-1]
                node = visited_nodes[0]
                edge_weight = self.graph.get_edge_data(prev_node, node)["weight"]
                sol += str(prev_node) + " -> " + str(node) + " Weight: " + str(edge_weight) + "\n"

                sol += "Total cost: " + str(path_length)
                print(sol)
            else:
                print("No solution was found")

    def init_population(self, pop_size: int = 100):
        pop = []
        # Maximum amount of edges the traveling salesperson problem can use (I think)
        max_length = sum(range(len(self.graph.nodes))) + len(self.graph.nodes) - 1
        max_int = len(self.graph.nodes) - 1
        for i in range(pop_size):
            genome = IntString(length=max_length,
                               max_co=self.max_co,
                               max_int=max_int)
            pop.append(Individual(genome))
        return pop
