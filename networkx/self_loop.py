import networkx as nx
import numpy as np


def test1():
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

    print 'NetworkX version'
    print Ln_nx
    print '\nUsing G.degree to compute D'
    print Ln1
    print '\nUsing A.sum(1) to compute D'
    print Ln2
    print '\nUsing G.degree and nx.laplacian to compute D'
    print Ln3

def laplacian_matrix_aw(G, nodelist=None, weight='weight'):
    """Return the Laplacian matrix of G.

    The graph Laplacian is the matrix L = D - A, where
    A is the adjacency matrix and D is the diagonal matrix of node degrees.

    Parameters
    ----------
    G : graph
       A NetworkX graph 

    nodelist : list, optional       
       The rows and columns are ordered according to the nodes in nodelist.
       If nodelist is None, then the ordering is produced by G.nodes().

    weight : string or None, optional (default='weight')
       The edge data key used to compute each value in the matrix.
       If None, then each edge has weight 1.

    Returns
    -------
    L : NumPy array
      Laplacian of G.

    Notes
    -----
    For MultiGraph/MultiDiGraph, the edges weights are summed.
    See to_numpy_matrix for other options.

    See Also
    --------
    to_numpy_matrix
    normalized_laplacian
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError(
          "laplacian() requires numpy: http://scipy.org/ ")
    # this isn't the most efficient way to do this...
    if G.is_multigraph():
        A=np.asarray(nx.to_numpy_matrix(G,nodelist=nodelist,weight=weight))
        I=np.identity(A.shape[0])
        D=I*np.sum(A,axis=1)
        L=D-A
        return L
    # Graph or DiGraph, this is faster than above 
    if nodelist is None:
        nodelist=G.nodes()
    n=len(nodelist)
    index=dict( (n,i) for i,n in enumerate(nodelist) )
    L = np.zeros((n,n))
    for ui,u in enumerate(nodelist):
        totalwt=0.0
        for v,d in G[u].items():
            try:
                vi=index[v]
            except KeyError:
                continue
            wt=d.get(weight,1)
            L[ui,vi]= -wt
            if ui != vi:
                totalwt += wt
        L[ui,ui]= totalwt
    return L

def norm_lap_aw(G):
    A = nx.adj_matrix(G)
    D = np.array(np.sum(A,1)).flatten()
    Disqrt = np.array(1 / np.sqrt(D))
    Disqrt = np.diag(Disqrt)
    L = np.diag(D) - A

    print 'Matrices used by AJW'
    print 'L'
    print L
    print 'Disqrt'
    print Disqrt
    Ln = np.dot(Disqrt,np.dot(L,Disqrt))
    return Ln
    
def norm_lap(G, nodelist=None, weight='weight'):
    # Graph or DiGraph, this is faster than above 
    if nodelist is None:
        nodelist = G.nodes()
    n=len(nodelist)
    L = np.zeros((n,n))
    deg = np.zeros((n,n))
    index=dict( (n,i) for i,n in enumerate(nodelist) )
    for ui,u in enumerate(nodelist):
        totalwt=0.0
        for v,data in G[u].items():
            try:
                vi=index[v]
            except KeyError:
                continue
            wt=data.get(weight,1)
            L[ui,vi]= -wt
            if ui != vi:
                totalwt += wt
        print 'tw', totalwt
        L[ui,ui]= totalwt
        if totalwt>0.0:
            deg[ui,ui]= np.sqrt(1.0/totalwt)

    Lnx =  nx.laplacian(G)
    print 'Matriced used by NetworkX'
    print 'nx.laplacian(G)'
    print Lnx

    print '\nL'
    print L

    print 'Disqrt'
    print deg
    L=np.dot(deg,np.dot(L,deg))
    return L
    
if __name__ == '__main__x':
    N = 3;
    G = nx.cycle_graph(N)
    # Add self loop to all vertices
    for node in G.nodes():
        G.add_edge(node, node)

    Ln = norm_lap(G)
    Ln_aw = norm_lap_aw(G)

    print '\nNetworkX version'
    print Ln
    print 'AJW version'
    print Ln_aw

    
if __name__ == '__main__x':
    N = 3;
    G = nx.cycle_graph(N)

    print nx.laplacian(G)
    print laplacian_matrix_aw(G)
    
    # Add self loop to all vertices
    Gsl = G.copy()
    for node in Gsl.nodes():
        Gsl.add_edge(node, node)

    print nx.laplacian(Gsl)
    print laplacian_matrix_aw(Gsl)

if __name__ == '__main__':
    test1()
