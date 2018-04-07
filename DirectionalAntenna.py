"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import math


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, pattern_file_name=None, use_degrees=True, mirror=True):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32, np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.pattern_file_name = pattern_file_name
        self.resolution = 1
        self.pattern = None
        
        if pattern_file_name is not None:
            with open(pattern_file_name) as pattern_file:
                self.pattern = np.genfromtxt(pattern_file, dtype='float_', delimiter=',', skip_header=1)
            self.resolution = np.mean(np.diff(self.pattern[:, 0]))
            if not use_degrees:
                self.resolution *= math.pi / 180
            self.pattern = 10**(self.pattern[:,1]/20)
            if mirror:
                self.pattern = np.append(self.pattern, self.pattern[-1:1:-1])
            print('Pattern length:', self.pattern.size)

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = self.pattern[np.mod((input_items[0]/self.resolution).astype(int), self.pattern.size)] * input_items[1]
        return len(output_items[0])
