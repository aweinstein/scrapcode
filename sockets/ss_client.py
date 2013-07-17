"""
Client for the SocketServer.

Based on
http://docs.python.org/2/library/socketserver.html
"""
import socket
import sys
import time

def send_tcp(data, host, port):
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((host, port))
        sock.sendall(data + '\n')
        received = sock.recv(1024)
    finally:
        sock.close()

    return received

def send_udp(data, host, port):
    # Create a socket (SOCK_DGRAM means a UDP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data + '\n', (host, port))
    received = sock.recv(1024)
    return received

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9998
    data = ' '.join(sys.argv[2:])
    if sys.argv[1].lower() == 'tcp':
        received = send_tcp(data, HOST, PORT)

    if sys.argv[1].lower() == 'udp':
        received = send_udp(data, HOST, PORT)

    print 'Sent:     {}'.format(data)
    print 'Received: {}'.format(received)
