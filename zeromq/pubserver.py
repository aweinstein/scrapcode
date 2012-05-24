#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
#

import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:

    x = random.randint(0, 10)
    y = random.randint(0, 10)
    socket.send('(%d, %d)' % (x, y))
    time.sleep(1)
