#!/usr/bin/env python   
import socket
import time
import threading


#Fake logger class
class Logger:
    def info(self, s):
        print s
    def debug(self,s):
        print s
    def error(self, s):
        print s
    def critical(self,s):
        print s
logger = Logger()

class ClientConnection(threading.Thread):
    """Manage the communication with a particular client."""
    def __init__(self, conn, timeout=10):
        threading.Thread.__init__(self)
        self.conn = conn
        self.timeout = timeout
        self.running = True

    def stop(self):
        """Stop the thread execution."""
        self.running = False
        #self.conn.close()

    def run(self):
        connected = True
        self.conn.settimeout(self.timeout)
        while self.running and connected:
            try:
                data = self.conn.recv(256)
            except socket.timeout:
                self.running = False
                logger.critical('Connection timeout')
                break
            if not data:
                logger.critical('Connection closed')
                connected = False              
            else:
                self.process_data(data)
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()
        logger.info('Closing the connection socket')

    def process_data(self, data):
        logger.info(data)
        self.conn.send(data)
        ## if data.startswith('alarm'):
        ##     logger.info('Alarm received')
        ##     self.conn.send('ACK')
        ## else:
        ##     logger.info('Unknow command received')
        ##     self.conn.send('Unknow command')
        

class Server(threading.Thread):
    """TCP server."""
    def __init__(self, host='', port=62000, client_class=ClientConnection):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.client = client_class
        self.running = True

    def stop(self):
        """Stop the thread execution."""
        self.running = False
        # Make a connection to unblock the socket.accept() call
        logger.info('Creating a socket to force the closing')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(('localhost', self.port))
        except socket.error:
            pass

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        trials = 1
        listening = False
        max_trials = 10
        servers = []
        while trials <= max_trials:
            try:
                sock.bind((self.host, self.port))
                sock.listen(1)
            except socket.error, exc:
                logger.error('Error: %s' % exc)
                trials += 1
                time.sleep(5)
            else:
                trials = max_trials + 1
                listening = True
                logger.info('Listening on port %s' % self.port)

        if not listening:
            logger.critical("Error: Couldn't open the socket.")
            pass
        else:
            while self.running:
                # accept "call" from client
                conn, addr = sock.accept()
                # disable Nagle algorithm
                #conn.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
                logger.info('Received connection from '+ str(addr))
                # Start the TCP server
                server = self.client(conn) #ClientConnection(conn)
                server.setDaemon(True)
                server.start()
                servers.append(server)
        for server in servers:
            server.stop()
        sock.close()
        logger.info('Closing the listening socket')


if __name__ == "__main__":
#    logger = config_logger('rajant_server', auto_increment=False,
#                            console_level = logging.INFO)

    print 'starting the server'
    server = Server()
    server.setDaemon(True)
    server.start()
    
    try:
        while(1):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    print ' '
    server.stop()

