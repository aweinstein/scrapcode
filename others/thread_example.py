#!/usr/bin/env python
import time
import threading
import queue
import random

class Producer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.running = True
        self.q = q
        print('Producer thread started')

    def stop(self):
        """Stop the thread execution."""
        self.running = False
        print('Producer thread stopped')

    def run(self):
        while self.running:
            d = random.randint(1,100)
            self.q.put(d)
            time.sleep(0.1)

class Consumer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.running = True
        self.q = q
        print('Consumer thread started')

    def stop(self):
        """Stop the thread execution."""
        self.running = False
        print('Consumer thread stopped')

    def run(self):
        while self.running:
            d = self.q.get(True)
            print(d)


if __name__ == "__main__":

    q = queue.Queue()
    producer = Producer(q)
    producer.daemon = True
    producer.start()
    consumer = Consumer(q)
    consumer.daemon = True
    consumer.start()

    try:
        while(1):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    print(' ')
    producer.stop()
    consumer.stop()
