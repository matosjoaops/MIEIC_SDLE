import networkx as nx
import random
import sys
from networkx.algorithms.components.connected import is_connected

results = {}

for num in range(int(sys.argv[1])):
    for i in range(10, 110, 10):
        G = nx.Graph()
        for j in range(1, i + 1):
            G.add_node(j)
        while not is_connected(G):
            node1 = random.randint(1, i + 1)
            node2 = random.randint(1, i + 1)
            while node2 == node1:
                node2 = random.randint(1, i + 1)
            G.add_edge(node1, node2)
        with open(f"results{num + 1}.csv", "a") as csv:
            csv.write(f"{i},{len(G.edges)}\n")
        