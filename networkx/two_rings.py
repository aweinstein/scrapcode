import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import savemat

def two_rings():
    n = 64;
    n_rings = 2
    rings = n_rings * [nx.generators.classic.cycle_graph(n)]

    G = nx.Graph()
    for i in range(len(rings)):
        G = nx.disjoint_union(G, rings[i])

    # Find the middle vertex in each ring
    cc_v = nx.connected_components(G)
    i_c = [sorted(cc)[len(cc)/2] for cc in cc_v]

    G.add_edge(i_c[0], i_c[1])
    L = nx.spectrum.laplacian(G)
    A = nx.spectrum.adj_matrix(G)
    s = np.array(np.sum(A,1))
    D = np.diag(s[:,0])
    matlab_data = {'L':L,
                   'A': A,
                   'D': D}
    savemat('two_rings.mat',matlab_data)

#def n_rings():
if __name__ == '__main__':
    n = 32;
    n_rings = 5
    rings = n_rings * [nx.generators.classic.cycle_graph(n)]

    G = nx.Graph()
    for i in range(len(rings)):
        G = nx.disjoint_union(G, rings[i])

    # Find the middle vertex in each ring
    cc_v = nx.connected_components(G)

    for i in range(n_rings - 1):
        s = min(cc_v[i])
        d = (min(cc_v[i+1]) + max(cc_v[i+1])) / 2
        G.add_edge(s, d)
        
    L = nx.spectrum.laplacian(G)
    A = nx.spectrum.adj_matrix(G)
    s = np.array(np.sum(A,1))
    D = np.diag(s[:,0])
    matlab_data = {'L':L,
                   'A': A,
                   'D': D}
    savemat('five_rings.mat',matlab_data)
    #return G

if __name__ == '__main__x':
    G = n_rings()
