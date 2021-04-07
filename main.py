# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


# This class represent a node
class Node:

    # Initialize the class
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


# A* search

def A_Star(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    openNodes = []
    closedNodes = []
    openNodes.append(heuristics[start])

    while (len(openNodes) >0):

        openNodes.sort()
        _node = openNodes.pop(1)
        node = Node(_node)
        closedNodes.append(node)

        # Check if we have reached the goal, return the path (From Current Node to Start Node By Node.parent)
        if closedNodes==end:
            path =[]


            return path[::-1]
        # Return reversed path (Hint: Return Llist of path in this Fashion for Reverse return path[::-1])

        # Get neighbours
        neighbors = graph.get(node.name)

        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = value
            # Check if the neighbo is in the closed list
            if (neighbor in closedNodes):
                continue

            # Calculate cost to goal


            # Check if neighbor is in open list and if it has a lower f value
            if (In_Open(openNodes, neighbor) == True):
                openNodes.append(neighbor)
        # Everything is green, add neighbor to open list
    return
    # Return None, no path is found


# Check if a neighbor should be added to open list
def In_Open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True


# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
    graph.connect('Arad', 'Zerind', 75)
    # Add Remaining Links From Example Given in Sides (Romania Map)
    graph.connect('Fugaras', 'Bucharest', 211)
    graph.connect('Pitesti', 'Bucharest', 101)
    graph.connect('Giurgiu', 'Bucharest', 90)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance) for Destination Bucharest
    heuristics = {}
    heuristics['Arad'] = 366
    # Add Remaining Heuristics From Example Given in Sides (Romania Map)
    heuristics['Bucharest'] = 0

    # Print Graph Nodes
    print(graph.nodes())
    print('\n')

    # Run search algorithm
    path = A_Star(graph, heuristics, 'Arad', 'Bucharest')
    print('Paths')
    print(path)


# Tell python to run main method
if __name__ == "__main__": main()