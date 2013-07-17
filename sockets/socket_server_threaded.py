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
        #print 'Running in', cur_thread.name

class TCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    host, port = 'localhost', 9998

    if len(sys.argv) == 2:
        port = int(sys.argv[1])

    TCPServer.allow_reuse_address = True
    server = TCPServer((host, port), TCPHandler)
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
