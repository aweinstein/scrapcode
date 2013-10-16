import zmq
import time
import sys
import numpy as np

# send_array and recv_array based on
# http://zeromq.github.io/pyzmq/serialization.html
def send_array(socket, A, flags=0, copy=True, track=False):
    """Send a NumPy array with metadata"""
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    socket.send_json(md, flags|zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)

def recv_array(socket, flags=0, copy=True, track=False):
    """Receive a NumPy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = buffer(msg)
    A = np.frombuffer(buf, dtype=md['dtype'])
    return A.reshape(md['shape'])


def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    N = 15
    while True:
        try:
            #  Wait for next request from client
            message = socket.recv()
            print "Received request: ", message

            #  Do some 'work'
            if message == 'q':
                x = np.random.randint(0, 10, N)
                print 'Sending the NumPy array'
                print x
                send_array(socket, x)
            else: # Send reply back to client
                socket.send("World")
        except KeyboardInterrupt:
            print
            sys.exit(0)

def client():
    context = zmq.Context()

    #  Socket to talk to server
    print "Connecting to hello world server..."
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:5555")

    #  Do 10 requests, waiting each time for a response
    for request in range (1,10):
        print "Sending request ", request,"..."
        socket.send ("q")

        #  Get the reply.
        x = recv_array(socket)
        print "Received"
        print x
        time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Use as 'numpy_serializing.py client' or"
               "'numpy_serializing.py server'")
    elif sys.argv[1] == 'client':
        client()
    elif sys.argv[1] == 'server':
        server()
    else:
        print "Don't know what to do"
