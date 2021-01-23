#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt

G=nx.path_graph(4)
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw(G)
plt.savefig("out/netx02.png")

