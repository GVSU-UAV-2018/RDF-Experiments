#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import sys
import numpy
import math
import socket
import struct

from gnuradio import gr

RDF_INTERMEDIATE_PORT = 12659

num_bins = 1024
std_threshold = 20 #What determines signal exists
pulse_bin_start = 510 #Starting bin for where we are looking for pulse
pulse_bin_width = ((num_bins / 2) - pulse_bin_start) * 2 #Determine how wide the signal range should be -> 4 bins wide right now

class Pulse_Detect(gr.sync_block):
    """
    docstring for block Pulse_Detect
    """
    def __init__(self):
        global num_bins
        gr.sync_block.__init__(self,
            name="Pulse_Detect",
            in_sig=[(numpy.float32,num_bins)],
            out_sig=None)

    def work(self, input_items, output_items):
        global num_bins
        global snr_threshold
        global pulse_bin_start
        global pulse_bin_width
        
        signal_arr = numpy.array([])#(pulse_bin_start - 1):(pulse_bin_start + pulse_bin_width - 1)] #minus 1 because zero base array
        noise_arr = numpy.array([])
        
        for x in range (pulse_bin_start, pulse_bin_start + pulse_bin_width - 1):
            signal_arr = numpy.insert(signal_arr, 0, input_items[0][0,x])
        for x in range (0, pulse_bin_start - 1):
            noise_arr = numpy.insert(noise_arr, 0, input_items[0][0,x])
        for x in range (pulse_bin_start + pulse_bin_width, num_bins - 1):
            noise_arr = numpy.insert(noise_arr, 0, input_items[0][0,x])
            
            
        noise_mean = numpy.mean(noise_arr[0:num_bins - 1])
        signal_mean = numpy.mean(signal_arr[0:pulse_bin_width - 1])
        noise_std = numpy.std(noise_arr[0:num_bins - 1])
        total_std = numpy.std(input_items[0][0:num_bins - 1])
        
        signal_confidence = total_std / noise_std
            
        print("Noise Std: ", noise_std)
        print("Total Std: ", total_std)
        print("Confidence: ", signal_confidence)
        
        sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_send.sendto(struct.pack("!ffff", noise_mean, total_std, signal_mean, signal_confidence), ("localhost", RDF_INTERMEDIATE_PORT))
            
        return len(input_items[0])
