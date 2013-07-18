import argparse
import sys
import time
import threading
import SocketServer

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP/UDP client.')
    parser.add_argument('-n', '--host', action='store', default='localhost',
                        help='Server address')
    parser.add_argument('-p', '--port', action='store', type=int, default=9998,
                        help='Server port')
    parser.add_argument('-t', '--protocol', choices=['tcp', 'udp'], default='udp',
                        help='Protocol')
    args = parser.parse_args()

    host, port = args.host, args.port
    protocol = args.protocol

    if protocol == 'tcp':
        TCPServer.allow_reuse_address = True
        server = TCPServer((host, port), TCPHandler)

    if protocol == 'udp':
        server = UDPServer((host, port), UDPHandler)

    ip, port = server.server_address
    print 'ip: {}, port: {}'.format(ip, port)

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
