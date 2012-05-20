#!/usr/bin/env python

# Send the current IP to ocam.cl

import socket
from subprocess import Popen, PIPE, call
import re
import os
import time

def get_ifconfig():
    cmd = '/sbin/ifconfig'
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    return stdout

def parse_addr(ifc):
    lines = ifc.splitlines()
    inames = []
    iaddr = []
    ip_regex = 'addr:(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
    for line in lines:
        s = re.search('^[a-z0-9]+ ', line)
        if s:
            inames.append(s.group().strip())
        s = re.search(ip_regex, line)
        if s:
            iaddr.append(s.group().split(':')[1])
    return zip(inames, iaddr)

def make_string(addrs):
    s = [time.asctime() + '\n'] 
    for a in addrs:
        s.append('%s -> %s' % a)
    return '\n'.join(s) + '\n'


if __name__ == '__main__':    
    ifc = get_ifconfig()
    addrs = parse_addr(ifc)
    s = make_string(addrs)
    file_name = os.path.join('/tmp', socket.gethostname() + '.txt')
    f = open(file_name, 'w')
    f.write(s)
    f.close()
    cmd = '/usr/bin/scp'
    par = 'send_data@ocam.cl:/home/send_data/ip_info'
    print cmd
    try:
        call((cmd, file_name, par))
    except OSError as (errno, strerror):
        print "OS error({0}): {1}".format(errno, strerror)

