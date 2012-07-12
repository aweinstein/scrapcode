import matplotlib.pyplot as plt
import numpy as np
from scipy.special import legendre, eval_legendre, eval_sh_legendre


if __name__ == '__main__':

    # Legendre
    plt.figure(1)
    x = np.arange(-1, 1, 0.01)
    for n in range(6):
        p = eval_legendre(n, x)
        plt.plot(x, p)

    # Shifted to [0,1] Legendre 
    plt.figure(2)
    x = np.arange(0, 1, 0.01)
    for n in range(6):
        p = eval_sh_legendre(n, x)
        plt.plot(x, p)

    # Shifted to [0,A] Legendre
    plt.figure(3)
    A = 10
    f = lambda x: (2./A)*x - 1
    x = np.arange(0, A, 0.001)
    for n in range(6):
        p = eval_legendre(n, f(x))
        plt.plot(x, p)

    plt.show()
    print 'Done'
