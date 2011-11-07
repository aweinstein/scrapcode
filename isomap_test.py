import numpy as np
from sklearn import manifold

n = 1000;
m = 10;
X = np.random.rand(n,m)
n_neighbors = 5
out_dim = 3

print 'Using random data'
Y = manifold.Isomap(n_neighbors, out_dim).fit_transform(X)
print 'out_dim:%d Y shape: %s' % (out_dim, Y.shape)

print 'Using the data X.npy and Isomap'
X = np.load('X.npy')
Y = manifold.Isomap(n_neighbors, out_dim).fit_transform(X)
print 'out_dim:%d Y shape: %s' % (out_dim, Y.shape)


Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim).fit_transform(X)

print 'Using the data X.npy and LLE'
print 'out_dim:%d Y shape: %s' % (out_dim, Y.shape)

