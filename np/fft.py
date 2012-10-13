import sys
import numpy as np
import matplotlib.pyplot as plt

N = 128
f = int(sys.argv[1])
n = np.arange(0, N)
x = np.cos(2 * np.pi * n * f / N)
x_hat = np.fft.fft(x)

plt.close('all')
plt.subplot(211)
plt.stem(n, x)
plt.subplot(212)
plt.stem(n, np.abs(x_hat))
plt.show()
