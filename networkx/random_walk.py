import os

import networkx as nx
import numpy as np
import scipy.linalg.matfuncs


if __name__ == '__main__':

    print 'Analysing a random walk over a graph'

    # Load the graph, create if it does not exist
    fn = 'rw.gml'
    if os.path.isfile(fn):
        G = nx.read_gml(fn)
        print 'Loaded', fn
    else:
        n = 6
        m = 10
        G = nx.generators.random_graphs.gnm_random_graph(n, m)
        nx.write_gml(G, fn)
        print 'Created', fn

    A = nx.linalg.spectrum.adj_matrix(G)
    degs = nx.degree(G)
    D = np.diag([degs[key] for key in sorted(degs.iterkeys())])
    D = np.matrix(D)
    P = D**-1 * A
    Pi = P**40 # What's the right way to compute P^n n-> infinity?
    T = Pi**-1 * P * Pi
    D_sqrt = np.matrix(scipy.linalg.matfuncs.sqrtm(D))
    T = D_sqrt * P * D_sqrt**-1
    T = np.real(T)
