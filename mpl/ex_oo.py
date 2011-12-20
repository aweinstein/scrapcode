import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax.plot(t, s1, 'b-')
ax.set_xlabel('time (s)')
plt.show()
