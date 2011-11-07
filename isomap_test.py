import numpy as np
from sklearn import manifold

n = 1000;
m = 10;
X = np.random.rand(n,m)
n_neighbors = 5
out_dim = 3


Y = manifold.Isomap(n_neighbors, out_dim).fit_transform(X)
print 'Using random data and Isomap'
print 'X shape:%s, out_dim:%d, Y shape: %s' % (X.shape, out_dim, Y.shape)

X = np.load('X.npy')
Y = manifold.Isomap(n_neighbors, out_dim).fit_transform(X)
print
print 'Using the data X.npy and Isomap'
print 'X shape:%s, out_dim:%d, Y shape: %s' % (X.shape, out_dim, Y.shape)

Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim).fit_transform(X)
print
print 'Using the data X.npy and LLE'
print 'X shape:%s, out_dim:%d, Y shape: %s' % (X.shape, out_dim, Y.shape)

