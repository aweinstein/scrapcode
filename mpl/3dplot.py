from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#X, Y, Z = axes3d.get_test_data(0.1)
x = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, x)
Z = np.sqrt(X**2 + Y**2)
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)

plt.figure()
x = np.linspace(-5, 5, 1000)
y = np.sqrt(x**2)
plt.plot(x, y)

plt.show()
