"""Computing the left eigenvector of a non-negative matrix. We find
the left eigenvector corresponding to the biggest eigenvalue, i.e.,
the Perron vector, and normalize so it has unit sum."""

import numpy as np

A = np.array([[0.8147, 0.0975, 0.1576, 0.1419, 0.6557],
              [0.9058, 0.2785, 0, 0.4218, 0.0357],
              [0.1270, 0.5469, 0.9572, 0.9157, 0.8491],
              [0, 0.9575, 0.4854, 0.7922, 0.9340],
              [0.6324, 0.9649, 0.8003, 0.9595, 0.6787]])
evals, evecs = np.linalg.eig(A.T)
rho = evals.max()
phi = evecs[:, evals==rho]
phi /= phi.sum()  # Normalize to unit sum, so it is the Perron vector

# Sanity check
print np.dot(phi.T, A)
print rho * phi.T
