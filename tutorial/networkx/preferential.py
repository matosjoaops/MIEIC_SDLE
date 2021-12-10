import networkx as nx
import random
import sys
import matplotlib.pyplot as plt
from networkx.algorithms.components.connected import is_connected

def count_edges(num_nodes):
    G = nx.Graph()
    
    for i in range(1, num_nodes + 1):
        G.add_node(i)
        
    while not is_connected(G):
        
        original_nodes = list(G.nodes)
        node_lottery = list(G.nodes)
        
        for node in original_nodes:
            degree = len(G.adj[node])
            for _ in range(degree):
                node_lottery.append(node)
        
        node1 = node_lottery[random.randint(0, len(node_lottery) - 1)]
        node2 = node_lottery[random.randint(0, len(node_lottery) - 1)]
        while node1 == node2:
            node2 = node_lottery[random.randint(0, len(node_lottery) - 1)]
        
        G.add_edge(node1, node2)

    return G.number_of_edges()
        
num_iterations = int(sys.argv[1])
iterations = []

for i in range(10, 110, 10):
    
    sub_iterations = []
    for _ in range(num_iterations):
        sub_iterations.append(count_edges(i))
    iterations.append(sub_iterations)
    
labels = [10,20,30,40,50,60,70,80,90,100]
plt.boxplot(iterations, labels = labels)
plt.savefig("preferential.png")
        
    
