import socket
import sys
import time
import threading
import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = '{}: {}'.format(cur_thread.name, data)
        self.request.sendall(response.upper())
        print 'Running in', cur_thread.name

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
         socket.sendto(data.upper() + ' ' + time.asctime(), self.client_address)

class UDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == '__main__':
    host, port = 'localhost', 9998

    if len(sys.argv) == 3:
        port = int(sys.argv[2])

    if sys.argv[1].lower() == 'tcp':
        TCPServer.allow_reuse_address = True
        server = TCPServer((host, port), TCPHandler)

    if sys.argv[1].lower() == 'udp':
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
