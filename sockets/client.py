#!/usr/bin/env python

"""
Echo client program

Example (run each command in a different terminal):
$ python server_multithread.py
$ python client.py --port 62000 --delay 2000
$ python client.py --port 62000 --delay 2000
"""
import socket
import sys
import string
import time
import random
from optparse import OptionParser


parser = OptionParser()
parser.add_option('--host', action='store', type='string', dest =
                   'host', default='localhost', help='Server host.')
parser.add_option('--port', action='store', type='int', dest =
                   'port', default=50007, help='Server port.')
parser.add_option('--packet_size', action='store', type='int', dest =
                   'packet_size', default=4096, help='Packet size')
parser.add_option('--delay', action='store', type='int', dest =
                   'delay', default=0, help='Delay in milliseconds')
(options, args) = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((options.host, options.port))
alphanum = string.digits + string.letters
ndata = 0
start = time.time()
elapsed = 0
packet_size = options.packet_size
delay = options.delay / 1000.0
try:
    while 1:
        c =''.join([random.choice(alphanum) for x in range(packet_size)])
        s.send(c)
        data = s.recv(packet_size)
        ndata += len(data)
        delta_t = time.time() - start
        if delta_t > 1.0:
            elapsed += delta_t
            kbs = (ndata / delta_t) / 1000.0
            print 'Elapsed: %.0f KBS: %.1f' % (elapsed, kbs)
            ndata = 0
            start = time.time()
        if delay > 0:
            time.sleep(delay)
except KeyboardInterrupt:
    pass

s.close()
