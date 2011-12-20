import networkx as nx
import scipy.sparse
import numpy as np



def mypr(G, alpha=0.85, personalization=None,
       max_iter=100, tol=1.0e-6, weight='weight'):

    nodelist=G.nodes()
    M=nx.to_scipy_sparse_matrix(G,nodelist=nodelist,weight=weight)
    (n,m)=M.shape # should be square

    S = scipy.array(M.sum(axis=1))
    S[S>0] = 1.0 / S[S>0]
    Sm = scipy.sparse.lil_matrix((n,n))
    Sm.setdiag(S.flat)
    Sm = Sm.tocsr()
    M = Sm * M

    ## Q = scipy.sparse.spdiags(S.T, 0, *M.shape, format='csr')
    ## M = Q * M
    
    x=scipy.ones((n))/n  # initial guess
    dangle=scipy.array(scipy.where(M.sum(axis=1)==0,1.0/n,0)).flatten()
    # add "teleportation"/personalization
    v=x
    i=0
    while i <= max_iter:
        # power iteration: make up to max_iter iterations
        xlast=x
        x=alpha*(x*M+scipy.dot(dangle,xlast))+(1-alpha)*v
        x=x/x.sum()
        # check convergence, l1 norm            
        err=scipy.absolute(x-xlast).sum()
        if err < n*tol:
            r = dict(zip(nodelist,x))
            return r
        i+=1
    
    print 'Failed to converge'

def mypr2(G, alpha=0.85, personalization=None,
       max_iter=100, tol=1.0e-6, weight='weight'):

    nodelist=G.nodes()
    M=nx.to_scipy_sparse_matrix(G,nodelist=nodelist,weight=weight)
    (n,m)=M.shape # should be square

    S = scipy.array(M.sum(axis=1))
    S[S>0] = 1.0 / S[S>0]
    Q = scipy.sparse.spdiags(S.T, 0, *M.shape, format='csr')
    M = Q * M
    
    x=scipy.ones((n))/n  # initial guess
    dangle=scipy.array(scipy.where(M.sum(axis=1)==0,1.0/n,0)).flatten()
    # add "teleportation"/personalization
    v=x
    i=0
    while i <= max_iter:
        # power iteration: make up to max_iter iterations
        xlast=x
        x=alpha*(x*M+scipy.dot(dangle,xlast))+(1-alpha)*v
        x=x/x.sum()
        # check convergence, l1 norm            
        err=scipy.absolute(x-xlast).sum()
        if err < n*tol:
            r = dict(zip(nodelist,x))
            return r
        i+=1
    
    print 'Failed to converge'




# Graph used as example in chapter 4 of "Google's PageRank and Beyond: The
# science of Search Engine Rankings", by Amy N. Langvilee and Carl D. Meyer

G = nx.DiGraph([(1,2), (1,3), (3,1), (3,2), (3,5), (4,5), (4,6), (5,4), (5,6),
                (6,4)])

#G = nx.gnm_random_graph(1000, 10000, directed=True)

pr_1 = nx.pagerank_scipy(G)
pr_2 = mypr(G)

## pr_1 = nx.pagerank(G, 0.9)
## pr_2 = nx.pagerank_scipy(G, 0.9)
## pr_3 = pr(G, 0.9)
## # Try with a bigger graph
## n = 1000
## m = 10000
## D = nx.gnm_random_graph(n, m, directed=True)
