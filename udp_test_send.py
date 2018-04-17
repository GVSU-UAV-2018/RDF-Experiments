#! /usr/bin/python2

import socket
import struct

sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_send.sendto(struct.pack("!f", 90.0), ("localhost", 12905))
