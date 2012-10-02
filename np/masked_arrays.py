import numpy as np

np.random.seed(42) # Just to get always the same output

a = np.random.randint(-10, 10, (1, 10))
mask = np.zeros_like(a, dtype='bool')
a_masked = np.ma.masked_array(a)
a_masked[a <= 0] = np.ma.masked

print 'a:', a
print 'a.argmin():', a.argmin()
print 'a.min():',a.min()
print
print 'a_masked:', a_masked
print 'a_masked.argmin():', a_masked.argmin()
print 'a_masked.min():',a_masked.min()
