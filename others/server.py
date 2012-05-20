#!/usr/bin/env python
# Echo server program
import socket
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--port', action='store', type='int', dest =
                   'port', default=50007, help='Server port.')
parser.add_option('--packet_size', action='store', type='int', dest =
                   'packet_size', default=4096, help='Packet size')
(options, args) = parser.parse_args()

HOST = ''                 # Symbolic name meaning all available interfaces

connected = False
while 1:
    try:
        if not connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, options.port))
            s.listen(1)
            print 'Listening on port', options.port, 'packet size', options.packet_size
            conn, addr = s.accept()
            print 'Connected by', addr
            connected = True
            start = time.time()
        try:
            data = conn.recv(options.packet_size)
        except socket.error:
            connected = False
            conn.close()
        if not data:
            connected = False
            conn.close()
        else:
            try:
                conn.send(data)
            except socket.error:
                connected = False
                conn.close()
            else:
                delta_t = time.time() - start
                if delta_t > 1.0:
                    print time.asctime()
                    start = time.time()
    except KeyboardInterrupt:
        break
conn.close()
print 'Bye!'
