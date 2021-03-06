"""
Client for the SocketServer.

Based on
http://docs.python.org/2/library/socketserver.html
"""
import argparse
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

def send_broadcast_udp(data, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(data, ('255.255.255.255', port))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP/UDP client.')
    parser.add_argument('-n', '--host', action='store', default='localhost',
                        help='Server address')
    parser.add_argument('-p', '--port', action='store', type=int, default=9998,
                        help='Server port')
    parser.add_argument('-t', '--protocol', choices=['tcp', 'udp', 'mudp'],
                        default='udp',
                        help='Protocol')
    parser.add_argument('msg', nargs='+', help='Message to be send')
    args = parser.parse_args()

    host, port = 'localhost', 9998
    host, port = args.host, args.port
    protocol = args.protocol
    data = ' '.join(args.msg)

    print 'Connecting to {}:{} ...'.format(host,port)
    if protocol == 'tcp':
        print 'Sending using TCP ...'
        received = send_tcp(data, host, port)
    elif protocol == 'udp':
        print 'Sending using UDP ...'
        received = send_udp(data, host, port)
    elif protocol == 'mudp':
        print 'Sending using UDP broadcast.'
        send_broadcast_udp(data, port)
        received = ''

    print 'Sent:     {}'.format(data)
    print 'Received: {}'.format(received)
