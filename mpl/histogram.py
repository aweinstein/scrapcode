import matplotlib.pyplot as plt
import numpy as np

nmax = 10
data = reduce(lambda x,y: x + y, (10*[i] for i in range(1,nmax + 1)))

plt.subplot(311)
pdf1, bins1, _ = plt.hist(data, nmax/2, normed=True)
plt.subplot(312)
pdf2, bins2, _ = plt.hist(data, nmax, normed=True)
plt.subplot(313)
pdf3, bins3, _ = plt.hist(data, 2*nmax, normed=True)

print np.sum(pdf1 * np.diff(bins1))
print np.sum(pdf2 * np.diff(bins2))
print np.sum(pdf3 * np.diff(bins3))

plt.show()
