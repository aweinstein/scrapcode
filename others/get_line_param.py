#!/usr/bin/env python

import sys

print 'Line paramenters'
if len(sys.argv) == 5:
    try:
        x1 = float(sys.argv[1])
        y1 = float(sys.argv[2])
        x2 = float(sys.argv[3])
        y2 = float(sys.argv[4])
    except ValueError:
        print 'Error: All the parameters must be numbers.'
        sys.exit(-1)
else:
    print 'Error: There must be four parameters.'
    sys.exit(-1)

m =  (y2 - y1) / (x2 - x1)
b = y1 - m * x1
sign = '+' if b >= 0 else '-'
print 'y = %.3fx %s %.3f' % (m, sign , abs(b))