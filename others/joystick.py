#!/usr/bin/env python
from __future__ import with_statement
import time
import threading
import pygame


class ReadJoystick(threading.Thread):
    """Read the joystick and set the throttle/brake and steering."""
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        pygame.init()
        pygame.joystick.init()
        self.js = pygame.joystick.Joystick(0)
        self.js.init()
        self.lock = threading.Lock()
        self.steering = 0.0
        self.throttle = 0
        self.brake = 0
        self.direction = 0

    def stop(self):
        self.running = False

    def get_data(self):
        with self.lock:
            steering = self.steering
            brake = self.brake
            throttle = self.throttle
            direction = self.direction
        return {'steering': steering,
                'brake': brake,
                'throttle': throttle,
                'direction': direction}

    def run(self):
        last_throttle = self.js.get_axis(1)
        last_steering = self.js.get_axis(3)
        last_direction = self.js.get_button(12)
        new_data = False
        while self.running:
            print self.js.get_button(0)
            throttle = self.js.get_axis(1)
            steering = self.js.get_axis(3)
            direction = self.js.get_button(12)
            if abs(last_throttle - throttle) > 0.01:
                last_throttle = throttle
                new_data = True
            if abs(last_steering - steering) > 0.01:
                last_steering = steering
                new_data = True
            if last_direction != direction:
                last_direction = direction
                new_data = True
            if new_data:
                if throttle < 0:
                    brake = 0
                    #throttle = int(abs(throttle)*100)
                    throttle = int(abs(throttle)*85)
                else:
                    brake = int(throttle*100)
                    throttle = 0
                steering = 30.0 * steering
                with self.lock:
                    self.steering = steering
                    self.brake = brake
                    self.throttle = throttle
                    self.direction = direction
                new_data = False
                print 'throttle: %d brake: %d steering: %.2f direction %d' % \
                     (throttle, brake, steering, direction)
            for event in pygame.event.get():
                pass
            time.sleep(0.01)

if __name__ == '__main__':

    joystick = ReadJoystick()
    joystick.setDaemon(True)
    joystick.start()
    try:
        while(1):
            time.sleep(1)
            print joystick.get_data()
    except KeyboardInterrupt:
        print 'Terminating'
    joystick.stop()
    

