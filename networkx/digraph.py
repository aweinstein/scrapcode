import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([(1,2), (2,1), (2,3), (2,5), (3,5), (4,5), (5,4), (4,1)])

Dout_inv = np.diag([1.0/G.out_degree()[n] for n in G.nodes()])
A = nx.linalg.adj_matrix(G)
P = Dout_inv * A


