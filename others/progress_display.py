import time
import sys

## for i in range(10):
##     time.sleep(0.1)
##     print 'Downloading File FooFile.txt [%d%%]\r'%i,
##     sys.stdout.flush()

for i in range(50):
    sys.stdout.write("\rDownload progress: %d%%   " % (i) )
    sys.stdout.flush()
    time.sleep(0.1)
print
