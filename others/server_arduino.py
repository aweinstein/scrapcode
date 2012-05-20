#!/usr/bin/env python
import time
from optparse import OptionParser

import server_multithread
from send_mail import send_mail

class ClientConnection(server_multithread.ClientConnection):

    def process_data(self, data):
        server_multithread.logger.info(data)
        if data.startswith('Alarm'):
            server_multithread.logger.info('Alarm received')
            self.conn.send('ACK')
            send_mail()
        else:
            server_multithread.logger.info('Unknow command received')
            self.conn.send('Unknow command')
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--port', action='store', type='int', dest =
                      'port', default=50007, help='Server port.')
    parser.add_option('--packet_size', action='store', type='int', dest =
                      'packet_size', default=4096, help='Packet size')
    (options, args) = parser.parse_args()

    print 'starting the server'
    server = server_multithread.Server(client_class=ClientConnection)
    server.setDaemon(True)
    server.start()
    
    try:
        while(1):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    print ' '
    server.stop()


