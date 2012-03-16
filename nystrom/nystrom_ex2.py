"""
Nystrom approximation, as described in 

Fowlkes, C., Belongie, S., & Chung, F. (2004). Spectral grouping using the
Nystrom method. IEEE Trans. Pattern Analysis and Machine Intelligence, 26(2),
214-225.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm, pinv, svd, norm

def annulus_clump(n_annulus=100, n_clump=50, R=3.0):
    """Create annulus/clump dataset.

    Parameters
    ----------
    n_annulus : integer, optional (default to 100)
                Number of points in the annulus
    n_clump : integet,m optional (default to 50)
              Number of points in the clump
    R : float, optional (default to 2)
        Distance from the center of the clump and the edge of the annulus

    Returns
    -------
    annulus : ndarray
              Array with shape (`n_annulus`, 2) with the (x,y) coordinates of 
	      the annulus pointset.
    clump: ndarray
           Array with shape (`n_clump`, 2) with the (x,y) coordinates of the
	   clump pointset.
    """

    # Annulus
    r = 5.0 # radius of the annulus
    phis = 2 * np.pi * np.random.rand(n_annulus, 1)
    rs = r + 0.1 * np.random.randn(n_annulus, 1)
    x = rs * np.cos(phis)
    y = rs * np.sin(phis)
    annulus = np.hstack((x, y))

    # Clump
    x_center = r - R
    sigma = 0.4
    x = x_center + sigma * np.random.randn(n_clump, 1)
    y = sigma * np.random.randn(n_clump, 1)
    clump = np.hstack((x, y))
    
    return annulus, clump

def affinity(points_a, points_b=None, sigma=1):
    """Compute the affinity of the pointset.

    Parameters
    ----------
    points_a: ndarray
            n-by-2 pointset
    points_b: ndarray, optional (default to None)
              If not None, compute affinity between points_a and points_b

    Returns
    -------
    W : ndarray
        n-by-n affinity matrix
    """

    n = points_a.shape[0]
    gauss_dist = lambda x,y: np.exp(-norm(x - y)**2 /(2*sigma**2))

    if points_b is None:
	W = np.zeros((n, n))
	for i in range(n):
	    for j in range(n):
		if i <= j:
		    a = gauss_dist(points_a[i,:], points_a[j,:])
		    W[i, j] = a
		    W[j, i] = a
    else:
	m = points_b.shape[0]
	W = np.zeros((n, m))
	for i in range(n):
	    for j in range(m):
		a = gauss_dist(points_a[i,:], points_b[j,:])
		W[i, j] = a

    return W

def nystrom(A, B):
    n = A.shape[0]
    m = B.shape[1]

    d1 = np.vstack((A, B.T)).sum(0).reshape(1,n)
    d2 = (B.sum(0).reshape(1,m) + 
	  np.dot(B.T.sum(0).reshape(1,n), np.dot(pinv(A), B)))
    dhat = np.sqrt( 1 / np.hstack((d1, d2))).T
    A = A * np.dot(dhat[:n], dhat[:n].T)
    B = B * np.dot(dhat[:n], dhat[n:].T)
    Asi = sqrtm(pinv(A)).real
    Q = A + np.dot(Asi, np.dot(np.dot(B, B.T), Asi))
    U, L, T = svd(Q)
    V = np.dot(np.dot(np.dot(np.vstack((A, B.T)), Asi), U),
               pinv(np.sqrt(np.diag(L))))
    nvec = 2
    E = np.zeros((n+m, nvec))
    for i in range(nvec):
	E[:, i] = V[:,i+1] / norm(V[:,i])

    return E

def fisher_separation(x1, x2):
    """Fisher separation between two clusters.

    The fisher separtion is (u_1 - u_2)^2 / (s1^2 + s2^2), where u_1 and u_2
    are the means and s1^2 and s2^2 the variances of x1 and x2.
    
    Parameters
    ----------
    x1, x2: ndarray
            Data points with each cluster

    Returns
    -------
    J : float
        Fisher separation
    """

    m = (x1.mean() - x2.mean())**2
    s = x1.var() + x2.var()
    J = m / s

    return J

    
def experiment_2():
    import scipy.io
    data = scipy.io.loadmat('data.mat')
    A = data['A'].byteswap().newbyteorder()
    B = data['B'].byteswap().newbyteorder()
    d = nystrom(A, B)

def experiment_1():
    annulus, clump = annulus_clump()
    points = np.vstack((clump, annulus))

    N = points.shape[0]
    W = affinity(points, sigma=0.5)
    D = np.diag(W.sum(1))
    Dsi = np.sqrt(np.linalg.inv(D))
    Wn = np.dot(Dsi, np.dot(W, Dsi))
    L = np.eye(N) - Wn
    eigvals, eigvecs = np.linalg.eigh(L)
    i = np.argsort(eigvals)
    eigvals = eigvals[i]
    eigvecs = eigvecs[:,i]
    embedding = eigvecs[:,1]

    W_eigvals, W_eigvecs = np.linalg.eigh(Wn)
    i = np.argsort(W_eigvals)[::-1]
    W_eigvals = W_eigvals[i]
    W_eigvecs = W_eigvecs[:,i]
    W_embedding = W_eigvecs[:,1]

    fs = fisher_separation(embedding[:50], embedding[50:])
    print 'Fisher separation = %.2f' % fs

    # plotting
    plt.close('all')

    plt.scatter(annulus[:,0], annulus[:,1])
    plt.scatter(clump[:,0], clump[:,1], c='g')
    plt.axis('equal')
    plt.grid()

    plt.figure()
    plt.plot(range(50), embedding[:50], 'og')
    plt.plot(range(50, 150), embedding[50:], 'ob')

    ## plt.figure()
    ## plt.plot(W_embedding)
    ## plt.show()

    return locals()

    
def experiment_3():

    annulus, clump = annulus_clump()
    points = np.vstack((clump, annulus))
    #points = np.load('annulus_clump.npy')

    N = points.shape[0]
    # Shuffle the points. This way the first block of W is equal to A
    i_samples = np.random.permutation(N)

    ## i_samples = np.load('i_samples.npy')
    points = points[i_samples,:]

    sigma_affinity = 0.5
    W = affinity(points, sigma=sigma_affinity)
    D = np.diag(W.sum(1))
    Dsi = np.sqrt(np.linalg.inv(D))
    Wn = np.dot(Dsi, np.dot(W, Dsi))
    L = np.eye(N) - Wn
    eigvals, eigvecs = np.linalg.eigh(L)
    i = np.argsort(eigvals)
    eigvals = eigvals[i]
    eigvecs = eigvecs[:,i]
    embedding = eigvecs[:,1]

    W_eigvals, W_eigvecs = np.linalg.eigh(Wn)
    i = np.argsort(W_eigvals)[::-1]
    W_eigvals = W_eigvals[i]
    W_eigvecs = W_eigvecs[:,i]
    W_embedding = W_eigvecs[:,1]

    # sample points and use nystrom extension
    n_sample = 50
    A = affinity(points[:n_sample,:], sigma=sigma_affinity)
    B = affinity(points[:n_sample,:], points[n_sample:,:], 
                 sigma=sigma_affinity)
    E = nystrom(A, B)
    v1 = E[:,0] / norm(E[:,0])
    v2 = E[:,1] / norm(E[:,1])

    v1_sort = v1[np.argsort(i_samples)]
    embedding_sort = embedding[np.argsort(i_samples)]
    fs1 = fisher_separation(embedding_sort[:50], embedding_sort[50:])
    fs2 = fisher_separation(v1_sort[:50], v1_sort[50:])
    print 'Fisher separation %.1f %.1f' % (fs1, fs2)
    
    if norm(embedding - v1) > norm(embedding + v1):
        v1 *= -1
        v1_sort *= -1
    
    # plotting
    plt.close('all')
    
    plt.figure()
    plt.scatter(annulus[:,0], annulus[:,1], s=40, c=(0.9,0.9,0.9))
    plt.scatter(clump[:,0], clump[:,1], s=40,  c=(0.5, 0.5, 0.5))
    plt.scatter(points[:n_sample,0], points[:n_sample,1], c='k', marker='x')
    plt.axis('equal')
    plt.grid()
    plt.savefig('dataset.pdf')

    plt.figure()
    #plt.subplot(211)
    plt.plot(embedding)
    plt.plot(v1)

    plt.figure(figsize=(16,5))
    #plt.subplot(212)
    plt.plot(embedding_sort, c=(0.7,0.7,0.7), lw=2, label='eigenvector')
    plt.plot(v1_sort, c='k', lw=1.1, label='Nystrom approximation')
    plt.xlim((0,N-1))
    plt.xlabel('Point number')
    plt.ylabel('Value of eigenvector')
    plt.legend()
    plt.savefig('eigenvector.pdf')

    plt.show()

    return locals()


if __name__ == '__main__':
    d = experiment_3()
    locals().update(d)

