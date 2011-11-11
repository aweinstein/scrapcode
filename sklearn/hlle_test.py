import numpy as np
from sklearn import manifold

n = 1000;
m = 50;
X = np.random.rand(n,m)
out_dim = 2
n_neighbors = 10
Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim,
                                    eigen_solver='dense',
                                    method='hessian').fit_transform(X)
print "Just computed HLLE using eigen_solver='dense'"
Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim,
                                    method='hessian').fit_transform(X)

## print
## print 'Using the data X.npy and LLE'
## X = np.load('X.npy')
## Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim).fit_transform(X)

## print
## print 'Using the data X.npy and HLLE'
## X = np.load('X.npy')
## Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim,
##                                     eigen_solver='dense',
##                                     method='hessian').fit_transform(X)



