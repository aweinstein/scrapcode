"""
SocketServer examples, based on
http://docs.python.org/2/library/socketserver.html
"""
import SocketServer
import sys

class TCPHandlerBase(SocketServer.BaseRequestHandler):
    """Instantiated once per connection."""
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print '{} wrote:'.format(self.client_address[0])
        print self.data
        # send back the same message but upper-cased
        self.request.sendall(self.data.upper())

class TCPHandlerStream(SocketServer.StreamRequestHandler):
    """Instantiated once per connection."""
    def handle(self):
        # self.rfile is a file-like object created by the handler
        self.data = self.rfile.readline().strip()
        print '{} wrote:'.format(self.client_address[0])
        print self.data
        # self.wfile is a file-like objest used to write back
        self.wfile.write(self.data.upper())

class UDPHandlerBase(SocketServer.BaseRequestHandler):
     def handle(self):
         data = self.request[0].strip()
         socket = self.request[1]
         print '{} wrote:'.format(self.client_address[0])
         print data
         socket.sendto(data.upper(), self.client_address)

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999

    if sys.argv[1].lower() == 'tcp':
        TCPHandler = TCPHandlerStream
        # Create the server, binding to `HOST` on `PORT`
        server = SocketServer.TCPServer((HOST, PORT), TCPHandler)

    if sys.argv[1].lower() == 'udp':
        UDPHandler = UDPHandlerBase
        server = SocketServer.UDPServer((HOST, PORT), UDPHandler)

    # Activate. Stop with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
