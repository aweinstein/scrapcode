#!/usr/bin/env python
import sys
import time

def print_elapsed(elapsed):
    secs = elapsed % 60
    mins = (elapsed % 3600) / 60
    hours = elapsed / 3600
    sys.stdout.write('\r%d:%02d:%02d ' % (hours, mins, secs))
    sys.stdout.flush()
    
started = time.time()

while True:
    try :
        now = time.time()
        elapsed = time.time() - started
        print_elapsed(elapsed)
        time.sleep(1 - (time.time() - now))
    except KeyboardInterrupt:
        print
        sys.exit()
