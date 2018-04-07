#! /usr/bin/python2

import csv
import struct
import socket

sock_direction = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_direction.bind(("localhost", 14342))
sock_direction.setblocking(0)

sock_rdf_samples = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rdf_samples.bind(("localhost", 12659))

last_known_direction = None

with open("test_data.csv", "w") as data_file:

    data_recorder = csv.writer(data_file)
    data_recorder.writerow(
        ["noise mean", "noise stdev", "signal mean", "P(signal)"])

    while True:
        dir_pkt = None
        rdf_sample = None
        try:
            dir_pkt, addr = sock_direction.recvfrom(1472)
        except socket.error:
            """Ignore this..."""
        else:
            last_known_direction = struct.unpack("!f", dir_pkt[0])

        try:
            rdf_sample_pkt = sock_rdf_samples.recvfrom(1472)
            rdf_sample = struct.unpack("!ffff", rdf_sample_pkt[0])
        except socket.error:
            """Ignore this..."""
        else:
            data_recorder.writerow(rdf_sample)
