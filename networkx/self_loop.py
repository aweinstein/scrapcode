import networkx as nx
import numpy as np

N = 3;
G = nx.cycle_graph(N)
# Add self loop to all vertices
for node in G.nodes():
    G.add_edge(node, node)

Ln_nx = nx.normalized_laplacian(G)
L_nx = nx.laplacian(G)

A = nx.adj_matrix(G)

# Using G.degree to compute D
D1 = np.array([G.degree()[n] for n in G])
Disqrt1 = np.array(1 / np.sqrt(D1))
Disqrt1 = np.diag(Disqrt1)
L1 = np.diag(D1) - A
Ln1 = np.dot(np.dot(Disqrt1, L1), Disqrt1)

# Using A.sum(1) to compute D
D2 = np.array(np.sum(A,1)).flatten()
Disqrt2 = np.array(1 / np.sqrt(D2))
Disqrt2 = np.diag(Disqrt2)
L2 = np.diag(D2) - A
Ln2 = np.dot(np.dot(Disqrt2, L2), Disqrt2)

# Using G.degree and nx.laplacian to compute D
L3 = nx.laplacian(G)
Ln3 = np.dot(np.dot(Disqrt1, L3), Disqrt1)
Ln3_ = np.dot(Disqrt1, np.dot(L3, Disqrt1))
