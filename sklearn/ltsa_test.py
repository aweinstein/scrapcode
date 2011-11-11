import numpy as np
from sklearn import manifold

n = 1000;
m = 3;
X = np.random.rand(n,m)
out_dim = 2
n_neighbors = 6
print 'Using random data and LTSA'
Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim,
                                    eigen_solver='dense',
                                    method='ltsa').fit_transform(X)

## print
## print 'Using the data X.npy and LLE'
## X = np.load('X.npy')
## Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim).fit_transform(X)

print
print 'Using the data X.npy and HLLE'
X = np.load('X.npy')
Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim,
                                    eigen_solver='dense',
                                    method='ltsa').fit_transform(X)
print Y.shape


