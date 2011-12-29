from itertools import combinations

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy.linalg import norm

def points_in_circle(n, add_noise=False):
    """Generate `n` points lying in a unit circle."""

    #phis = np.random.rand(n, 1) * 2 * np.pi

    ## phis = np.arange(0, 2*np.pi, 2*np.pi/n).reshape(n, 1)
    ## x = np.cos(phis)
    ## y = np.sin(phis)

    phis = np.arange(0, 2*np.pi, 2*np.pi/n).reshape(n, 1)
    rs = np.ones((n, 1))
    if add_noise:
        phis += 0.02 * np.random.randn(n, 1)
        rs += 0.02 * np.random.randn(n, 1)
    x = rs * np.cos(phis)
    y = rs * np.sin(phis)

    return np.hstack((x, y))

def weight(pair, sigma=1.0):
    """Weight between two points.

    The weight for point x and y is given by exp(-||x-y||^2/sigma).
    
    Parameters
    ----------
    pair : tuple of points
    sigma : real, default to 1.0

    Return
    ------
    w : real
    """
    w = np.exp(-norm(pair[1] - pair[0])**2 / sigma)

    return w
        
def graph(points):
    """Construct a graph from a point set.

    Parameters
    ----------
    points: n-by-m matrix
            A matrix with n points. Each point has dimension m

    Returns
    -------
    G : undirected graph
        The nodes of the graph are the points. There is an edge between two
    points if the distance between them is smaller than `delta`.
        
    """
    G = nx.Graph()

    delta = 0.3
    for pair in combinations(points, 2):
        d = norm(pair[1] - pair[0])
        if  d < delta:
            w = weight(pair)
            G.add_edge(tuple(pair[1]), tuple(pair[0]), weight=w)

    return G
        
        
if __name__ == '__main__':

    points = points_in_circle(30, add_noise=True)

    G = graph(points)
    nodes = [tuple(p) for p in points]
    L = nx.normalized_laplacian(G, nodelist=nodes)
    #L = nx.normalized_laplacian(G)
    L = (L + L.T) / 2.0 # iron out numerical wrinkles
    eigvals, eigvecs = np.linalg.eigh(L)

    new_point = np.array([0.8, 0.8])
    neighbors = []
    weights = {}
    delta = 0.3
    for n, p in enumerate(points):
        d = norm(p - new_point)
        if d < delta:
            w = weight((new_point, p))
            neighbors.append((n, w))

    i = 1 # approximate the second eigenvector
    phi = eigvecs[:,i]
    Lambda = eigvals[i]
    phi_x = 0
    dx = sum(w for _, w in neighbors)
    for n, w in neighbors:
        # I am not sure if the sum to compute dy should consider the new
        # point or not
        dy = sum(e[2]['weight'] for e in G.edges(nodes[n], data=True))
        phi_x += w * phi[n] / np.sqrt(dx * dy)
    phi_x /= Lambda
    
    # Plot
    plt.close('all')
    pos = dict([(tuple(p), (p[0],p[1])) for p in points])
    nx.draw(G, pos=pos, with_labels=False, node_size=75)
    plt.axis('equal')
    plt.plot(new_point[0], new_point[1], 'ob')
    for n, _ in neighbors:
        #plt.plot(p[0], p[1], 'xb')
        plt.plot(points[n,0], points[n,1], 'xb')
    plt.show()
    
    
