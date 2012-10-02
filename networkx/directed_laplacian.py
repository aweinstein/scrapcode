import networkx as nx

if __name__=='__main__':
#    import laplacian_spectral
    G = nx.DiGraph()
    G.add_cycle([1,2,3,4])
#    M = random_walk_matrix(G)
#    print M
#    M = pagerank_matrix(G)
#    print M
#    M = lazy_random_walk_matrix(G)
#    print M
#    print stationary_distribution(M)
    print nx.linalg.directed_laplacian(G)
