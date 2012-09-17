import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy import polyval

# Set the seed to get consistent results
np.random.seed(42)

def gen_data(d = 1, n=10, xmin=-1, xmax=1, sigma=0.5):
    """Use a polynomial linear model to generate noisy data.

    Generate noisy data of the form

    y_noisy = poly(d, x) + noise,

    where poly(d, x) is a polynomial of degree `d` evaluated at x, x is a
    vector of `n` points between `xmin' and `xmax`, and noisy is an iid normal
    vector with zero mean and variance `sigma`**2. The coefficients of the
    polynomial are choosen uniformly at random from the interval [1,2].

    Parameters
    -----------
    d: integer
        Degree of the polynomial.

    n: integer, optional
        Number of samples.

    xmin: float, optional
        Specify the minimum value of x.

    xmax: float, optional
        Specify the maximum value of x.

    sigma: float, optional
        Standar deviation of the noise.

    Returns
    --------
    x: array, shape: (n,)
        Independent variable.

    y: array, shape: (n, )
        Noiseless data.

    y_noise: array, shape: (n, )
        Noisy data.

    p: array, shape: (d+1, )
        Coefficientes of the polynomial.

    X: array, shape: (n, d+1)
        Feature matrix
    """
    p = np.random.rand(d+1) + 1
    x = np.linspace(xmin, xmax, n)
    y = polyval(p, x)
    y_noise = y + sigma * np.random.randn(10)
    X = np.array([[xx**n for n in range(d+1)] for xx in x])
    return x, y, y_noise, p, X


if __name__ == '__main__':
    d = 3
    x, y, y_noise, p, X = gen_data(d)
    clf = linear_model.LinearRegression(fit_intercept=False)
    clf.fit(X, y_noise)
    print clf.coef_[::-1]
    y_fit = clf.predict(X)

    plt.close('all')
    plt.plot(x, y, 'o:', label='original')
    plt.plot(x, y_noise, 'x:', label='noisy')
    plt.plot(x, y_fit, label='fit')
    plt.legend(loc='best')
    plt.show()
