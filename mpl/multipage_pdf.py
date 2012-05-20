import matplotlib.pyplot as plt
import matplotlib as mpl

params = {
    'text.usetex' : True,
    'font.family': 'serif',
    'font.serif' : ['Times'],
    }
mpl.rcParams.update(params)

plt.figure()
plt.plot([1,2,3])
plt.ylabel(r'$\alpha$')
plt.savefig('f1.pdf')
#plt.show()


