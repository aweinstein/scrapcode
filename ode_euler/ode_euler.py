'''
An implementation of Euler method for solving ODE.
'''
import numpy as np
import matplotlib.pyplot as plt


def ode_euler(f, y0, tf, h):
    '''Solve and ODE using Euler method.

    Solve the ODE y_dot = f(y, t)

    Parameters
    ----------
    f : function
        Function describing the ODE
    y0 : array_like
        Initial conditions.
    tf : float
        Final time.
    h : float
        Time step

    Returns
    -------
    y : array_like
        Solution to the ODE.
    t : array_like
        Time vector.
    '''
    y0 = np.array(y0)
    ts = np.arange(0, tf+h, h)
    y = np.empty((ts.size, y0.size))
    y[0,:] = y0
    for t, i in zip(ts[1:], range(ts.size - 1)):
        y[i+1,:] = y[i,:] + h * f(y[i,:], t)
    return y, ts
    

def newton_cooling(y, t):
    k = 1
    Tamb = 25
    return -k * (y - Tamb)

def vanderpol(y, t):
    mu = 1
    y1, y2 = y
    y1_dot = y2
    y2_dot = mu * (1 - y1**2) * y2 - y1
    return np.array((y1_dot, y2_dot))


def newton_cooling_example():
    print('Solving Newton Cooling ODE...')
    y, ts = ode_euler(newton_cooling, [50], 10, 0.01)
    print('Done.')
    plt.figure()
    plt.plot(ts, y)
    plt.xlabel('time [s]')
    plt.title('Solution to the Newton cooling equation')

def vanderpol_example():
    print('Solving van der Pol ODE...')
    y, ts = ode_euler(vanderpol, [2,0], 20, 0.01)
    print('Done.')
    plt.figure()
    plt.plot(ts, y)
    plt.xlabel('time [s]')
    plt.title('Solution to the van der Pol equation')

if __name__ == '__main__':
    newton_cooling_example()
    vanderpol_example()
    plt.show()
    

    
    
    
