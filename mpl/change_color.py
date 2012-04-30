import copy
import matplotlib.pyplot as plt

def base_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([1,2,3])
    ax.plot([2,3,1])
    plt.xlabel('x')
    plt.ylabel('y')

    return fig

fig1 = base_plot()
fig2 = base_plot()

l1 = fig2.axes[0].get_lines()[0]
l2 = fig2.axes[0].get_lines()[1]
l1.set_color('k')
l2.set_color('r')

plt.show()
