"""
Basic broadcast UDP example. Based on

http://stackoverflow.com/questions/12607516/python-udp-broadcast-not-sending
"""

from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
port = 54545
cs.sendto('This is a test', ('255.255.255.255', port))
print 'Done broadcasting on port', port
