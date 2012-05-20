from sklearn import manifold, datasets
#from sklearn.neighbors import NearestNeighbors

n_points = 1000
n_neighbors = 10
out_dim = 2

## nbrs = NearestNeighbors(n_neighbors=n_neighbors + 1)
## nbrs.fit(X)
## X = nbrs._fit_X

n_trials = 20
X, _ = datasets.samples_generator.make_s_curve(n_points, random_state=123)
for i in range(n_trials):
    print i

    Y = manifold.LocallyLinearEmbedding(n_neighbors, out_dim,
                                        eigen_solver='auto',
                                        method='standard').fit_transform(X)
    ## nbrs = NearestNeighbors(n_neighbors=n_neighbors + 1)
    ## nbrs.fit(X)
    ## X = nbrs._fit_X




