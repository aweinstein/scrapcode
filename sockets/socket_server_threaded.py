"""Socket server example.

Implements TCP, UDP and UDP broadcast server.

Note: When using an UDP server, a multicast address should be used. For example

$ python socket_server_threaded.py -n 226.1.1.3 -p 1234 -t mudp
"""
import argparse
import socket
import sys
import struct
import time
import threading
import SocketServer

# From https://github.com/nealjc/multicastserver/blob/master/multicastserver.py
class MulticastServer(SocketServer.UDPServer):
    """Extends UDPServer to join multicast groups and bind
    the local interface properly
    """

    def __init__(self, multicast_address, RequestHandlerClass,
                 listen_interfaces = None):
        """Create a new multicast server.

        multicast_address - two tuple ('multicast address', port)
        RequestHandlerClass - a SocketServer.BaseRequesetHandler
        listen_interfaces - list of local interfaces (identified by IP addresses)
        the server should listen on for multicast packets. If None,
        the system will decide which interface to send the multicast group join
        on
        """
        #to receive multicast packets, must bind the port,
        #set bind_and_active to True.
        #Note: some hosts don't allow bind()'ing to a multicast address,
        #so bind to INADDR_ANY
        SocketServer.UDPServer.allow_reuse_address = True
        SocketServer.UDPServer.__init__(self, ('', multicast_address[1]),
                                              RequestHandlerClass, True)

        #Note: struct ip_mreq { struct in_addr (multicast addr), struct in_addr
        #(local interface) }
        if listen_interfaces is None:
            mreq = struct.pack("4sI", socket.inet_aton(multicast_address[0]),
                               socket.INADDR_ANY)
            self.socket.setsockopt(socket.IPPROTO_IP,
                                       socket.IP_ADD_MEMBERSHIP, mreq)
        else:
            for interface in listen_interfaces:
                mreq = socket.inet_aton(
                    multicast_address[0]) + socket.inet_aton(interface)
                self.socket.setsockopt(socket.IPPROTO_IP,
                                       socket.IP_ADD_MEMBERSHIP, mreq)

    def server_close(self):
        #TODO: leave the multicast groups...
        pass

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        cur_thread = threading.current_thread()
        response = '{}: {}'.format(cur_thread.name, data)
        msg = 'Running in {}, received {} from {}'.format(cur_thread.name,
                                                          data, self.client_address)
        print msg
        resp = ' '.join([time.asctime(), data.upper()])
        print 'sending "{}" as response'.format(resp)
        self.request.sendall(resp)

class TCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class UDPHandler(SocketServer.BaseRequestHandler):
     def handle(self):
         data = self.request[0].strip()
         socket = self.request[1]
         cur_thread = threading.current_thread()
         client_address = self.client_address[0]
         msg = 'Running in {}, received {} from {}'.format(cur_thread.name,
                                                            data, client_address)
         print msg
         resp = ' '.join([time.asctime(), data.upper()])
         print 'sending "{}" as response'.format(resp)
         socket.sendto(resp, self.client_address)

class UDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

class UDPMultiServer(SocketServer.ThreadingMixIn, MulticastServer):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP/UDP client.')
    parser.add_argument('-n', '--host', action='store', default='localhost',
                        help='Server address')
    parser.add_argument('-p', '--port', action='store', type=int, default=9998,
                        help='Server port')
    parser.add_argument('-t', '--protocol', choices=['tcp', 'udp', 'mudp'],
                        default='udp', help='Protocol')
    args = parser.parse_args()

    host, port = args.host, args.port
    protocol = args.protocol

    if protocol == 'tcp':
        TCPServer.allow_reuse_address = True
        server = TCPServer((host, port), TCPHandler)

    if protocol == 'udp':
        server = UDPServer((host, port), UDPHandler)

    if protocol == 'mudp':
        server = UDPMultiServer((host, port), UDPHandler)

    ip, port = server.server_address
    print 'ip: {}, port: {}, protocol: {}'.format(ip, port, protocol.upper())

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print 'Server loop running in thread:', server_thread.name

    try:
        while(1):
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    server.shutdown()
    print 'Done'
