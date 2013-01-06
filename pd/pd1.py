import pandas as pd
from pandas import DataFrame
import numpy as np

df1 = DataFrame(np.arange(15).reshape((5, 3)),
                 ['T', 'F', 'T', 'T', 'F'],
                 columns=['one', 'two', 'three'])
print df1
print
print df1.ix['T']
print

df2 = DataFrame(np.arange(15).reshape((5, 3)),
                 [1, 0, 1, 1, 0],
                 columns=['one', 'two', 'three'])
print df2
print
print df1.ix[1]
