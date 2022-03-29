#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
        print "Usage: vrfy.py <username>"
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = open(sys.argv[1])
lines = file.readlines()
lines = [line.strip() for line in lines]
# Connect to the Server
connect = s.connect(('10.11.1.217',25))
# Receive the banner
banner = s.recv(1024)
print banner
for u in lines:
# VRFY a user
        s.send('VRFY ' + u + '\r\n')
        result = s.recv(1024)

        print result
# Close the socket
s.close()
