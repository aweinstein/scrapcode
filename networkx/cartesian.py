'''
Theorem 3 of

Mahadevan, S., & Maggioni, M. (2007). Proto-value functions: A Laplacian
framework for learning representation and control in Markov decision
processes. Journal of Machine Learning Research, 8

states that the eigenvalues of the Laplacian of graph G that is the cartesian
product of two graphs G1 and G2, are the sums of all the combination of the
eigenvalues of G1 and G2.

This program illustrates this by generating a grid as the cartesian product of
two paths.
'''

from itertools import product
import networkx as nx

n = 5
P = nx.path_graph(n)
G = nx.cartesian_product(P, P)

ev_P = nx.laplacian_spectrum(P)
ev_G = nx.laplacian_spectrum(G).real

ev = []
for i,j in product(range(n), repeat=2):
    ev.append(ev_P[i] + ev_P[j])


