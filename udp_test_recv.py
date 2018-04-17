#! /usr/bin/python2

import socket

sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind(("localhost", 42180))

while True:
    data, addr = sock_recv.recvfrom(1024)
    print("received message: ", data)
