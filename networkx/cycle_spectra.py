import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 16;
    x_k = lambda u,k,n: np.sin(2*np.pi*k*u/n)
    y_k = lambda u,k,n: np.cos(2*np.pi*k*u/n)
    u = np.arange(1, n+1)

    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.scatter(x_k(u,1,n), y_k(u,1,n))
    plt.axis('equal')
    xl = plt.xlim()
    yl = plt.ylim()
    ax.hlines(0, xl[0], xl[1], linewidth=0.1)
    ax.vlines(0, yl[0], yl[1], linewidth=0.1)
    plt.xlim(xl)
    plt.ylim(yl)

    ax = fig.add_subplot(122)
    ax.scatter(x_k(u,3,n), y_k(u,3,n))
    plt.axis('equal')
    xl = plt.xlim()
    yl = plt.ylim()
    ax.hlines(0, xl[0], xl[1], linewidth=0.1)
    ax.vlines(0, yl[0], yl[1], linewidth=0.1)
    plt.xlim(xl)
    plt.ylim(yl)

    plt.show()
