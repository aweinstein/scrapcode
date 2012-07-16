import copy
import sys

import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import pywt

import pltutils

import matplotlib as mpl
params = {'axes.labelsize': 18,
          'axes.titlesize': 20,
          'text.fontsize': 22,
          'legend.fontsize': 14,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          }
mpl.rcParams.update(params)


print 'Computing the wavelet coefficients...'

im_name = 'lenax'

if im_name == 'lena':
    image = scipy.misc.lena().astype('float32')
else:
    fn = 'valpo2.jpg'
    image = plt.imread(fn)
    #image = image.sum(2) # convert to gray scale
    image = image[::-1,:]

N = image.shape[0] * image.shape[1]

wavelet = pywt.Wavelet('db6')
levels = int( np.floor( np.log2(image.shape[0]) ) )

wc = pywt.wavedec2( image, wavelet, level=levels)
wc_flat = np.abs(np.concatenate([np.concatenate(c).flatten() for c in wc]))
wc_flat = np.sort(wc_flat)[::-1]

keep = 0.1
thr = wc_flat[int(N*keep)]

wc_approx = copy.deepcopy(wc)

for j in range(1, levels+1):
    for i in range(3):
        x = wc_approx[j][i]
        x[np.abs(x) < thr] = 0

image_approx = pywt.waverec2(wc_approx, wavelet)

f1 = plt.figure()
plt.imshow(image, cmap=cm.gray)
plt.yticks([])
plt.xticks([])
plt.title('Imagen original, %d pixels' % N)


f2 =plt.figure()
plt.semilogy(wc_flat, lw=2)
plt.ylim(ymin=1e-1)
plt.xlim(xmin=-20000, xmax=N)
plt.xticks([])
plt.title('Coeficientes Wavelets, ordenados por magnitud')
plt.tight_layout()

f3 = plt.figure()
plt.imshow(image_approx, cmap=cm.gray)
plt.yticks([])
plt.xticks([])
plt.title('Aproximacion usando %d%% de los coeficientes' % (keep*100,))

pltutils.save_figs_as_pdf([f1, f2, f3], 'sparse_image.pdf')





