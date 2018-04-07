"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import struct
import socket
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, udp_addr='localhost', udp_port=12904):
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=None,
            out_sig=[np.float32]
        )
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.sock.bind((udp_addr, udp_port))
        except:
            pass
        self.sock.setblocking(0)
        self.value = 0

    def work(self, input_items, output_items):
        data = self.value
        """example: multiply with constant"""
        try:
            data, addr = self.sock.recvfrom(1472)
        except socket.error:
            """Ignore this..."""
        else:
            self.value = struct.unpack("!f", data)
            
        output_items[0][:] = self.value
        return len(output_items[0])
