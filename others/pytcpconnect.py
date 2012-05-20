#!/usr/bin/env python

# Echo client program
import socket
import sys
import string
import struct
import time
import random
from optparse import OptionParser

def get_packet():
    header = '$start$:'
    type = 1
    length = 29
    status = 1
    throttle = 0
    brake = 0
    angle = -5.0
    direction = 1
    bumper = 0
    
    return header + struct.pack('>HLL2BfBL',
                                        type,
                                        length,
                                        status,
                                        throttle,
                                        brake,
                                        angle,
                                        direction,
                                        bumper)
def parse_packet(pckt):
    header = struct.unpack('>8sHL', pckt[0:14])
    type = header[1]
    if type == 0x00:
        parse_system_packet(pckt[10:])
    elif type == 0x01:
        d = parse_control_packet(pckt[10:])
        print d
    else:
        print 'Error: packet type unknown.'

def parse_system_packet(pckt):
    fmt = '>LHff'
    data = struct.unpack(fmt, pckt)
    min_steering = data[2]
    max_steering = data[3]
    print min_steering, max_steering
    
def parse_control_packet(pckt):
    fmt = '>3LBBfBB6Ll3LB'
    data = struct.unpack(fmt, pckt)
    fields = {'time_stamp': data[2],
              'throttle': data[3],
              'brake': data[4],
              'steering': data[5],
              'direction': data[6],
              'drive_mode': data[7],
              'encoder': data[14],
              'overflow': data[18]}
    
    return fields

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--host', action='store', type='string', dest =
                       'host', default='cRIO', help='Server host.')
    parser.add_option('--port', action='store', type='int', dest =
                       'port', default=6340, help='Server port.')
    parser.add_option('--packet_size', action='store', type='int', dest =
                       'packet_size', default=4096, help='Packet size')
    parser.add_option('--delay', action='store', type='int', dest =
                       'delay', default=0, help='Delay in milliseconds')
    (options, args) = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((options.host, options.port))
    s.settimeout(0.5)
    packet_size = options.packet_size

    i = 1
    try:
        while 1:
            if i % 2:
                pckt = get_packet()
                print 'Sending control packet.'
            else:
                pckt = '$start$:' + '\x00'*5 + '\x10\x55\xAA'
                print 'Sending system packet.'
            #i += 1

            s.send(pckt)
            try:
                data = s.recv(packet_size)
            except socket.timeout:
                pass
            else:
                #print 'Packet length: ', len(data)
                parse_packet(data)
            print
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    s.close()

