import matplotlib.pyplot as plt
import matplotlib as mpl

params = {'backend': 'Agg',
          'axes.labelsize': 18,
          'text.fontsize': 22,
          'legend.fontsize': 14,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          #'savefig.dpi' : 600,
          #'ps.usedistiller' : 'xpdf',
          'text.usetex' : True,
          #'font.family': 'serif',
          #'font.serif' : ['Times'],
          }
mpl.rcParams.update(params)


plt.plot([1,2,3])
plt.xlabel(r'$\|x\|$')
plt.show()
