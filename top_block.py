#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Apr  7 17:25:19 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import DirectionalAntenna
import DirectionalAntenna_1
import math
import scipy
import sip
import sys
import udp_repeat_source
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.pulse_samp_rate = pulse_samp_rate = 1000
        self.pulse_period_1 = pulse_period_1 = 1
        self.pulse_period_0 = pulse_period_0 = 1
        self.pulse_period_ticks_1 = pulse_period_ticks_1 = int(math.ceil(pulse_period_1 * pulse_samp_rate))
        self.pulse_period_ticks_0 = pulse_period_ticks_0 = int(math.ceil(pulse_period_0 * pulse_samp_rate))
        self.pulse_duty_1 = pulse_duty_1 = 0.2
        self.pulse_duty_0 = pulse_duty_0 = 0.2
        self.tuner_freq = tuner_freq = 150000000
        self.receiver_samp_rate = receiver_samp_rate = 3000000
        self.pulse_samp_rate_1 = pulse_samp_rate_1 = 1000
        self.pulse_duty_ticks_1 = pulse_duty_ticks_1 = int(math.floor(pulse_duty_1 * pulse_period_ticks_1))
        self.pulse_duty_ticks_0 = pulse_duty_ticks_0 = int(math.floor(pulse_duty_0 * pulse_period_ticks_0))
        self.noise_correction_factor = noise_correction_factor = 100
        self.network_decim = network_decim = 16
        self.n_adc_bits = n_adc_bits = 10.4
        self.freq_1 = freq_1 = 150000000
        self.freq_0 = freq_0 = 150000000
        self.direction_1 = direction_1 = 0
        self.direction_0 = direction_0 = 0
        self.SNR = SNR = 50

        ##################################################
        # Blocks
        ##################################################
        self._tuner_freq_range = Range(148000000, 152000000, 10000, 150000000, 200)
        self._tuner_freq_win = RangeWidget(self._tuner_freq_range, self.set_tuner_freq, "tuner_freq", "counter_slider", float)
        self.top_layout.addWidget(self._tuner_freq_win)
        self._freq_1_range = Range(148000000, 152000000, 100000, 150000000, 200)
        self._freq_1_win = RangeWidget(self._freq_1_range, self.set_freq_1, 'Signal 1 Freq', "counter_slider", float)
        self.top_layout.addWidget(self._freq_1_win)
        self._freq_0_range = Range(148000000, 152000000, 100000, 150000000, 200)
        self._freq_0_win = RangeWidget(self._freq_0_range, self.set_freq_0, 'Signal 0 Freq', "counter_slider", float)
        self.top_layout.addWidget(self._freq_0_win)
        self._direction_1_range = Range(0, 360, 1, 0, 1)
        self._direction_1_win = RangeWidget(self._direction_1_range, self.set_direction_1, 'Signal 1 Direction', "counter_slider", float)
        self.top_layout.addWidget(self._direction_1_win)
        self._direction_0_range = Range(0, 360, 1, 0, 1)
        self._direction_0_win = RangeWidget(self._direction_0_range, self.set_direction_0, 'Signal 0 Direction', "counter_slider", float)
        self.top_layout.addWidget(self._direction_0_win)
        self._SNR_range = Range(0, 100, 1, 50, 200)
        self._SNR_win = RangeWidget(self._SNR_range, self.set_SNR, "SNR", "counter_slider", float)
        self.top_layout.addWidget(self._SNR_win)
        self.udp_repeat_source = udp_repeat_source.blk(udp_addr='localhost', udp_port=12905)
        self.qtgui_sink_x_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	tuner_freq, #fc
        	receiver_samp_rate / network_decim, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)

        self.qtgui_sink_x_1.enable_rf_freq(False)



        self._pulse_period_1_tool_bar = Qt.QToolBar(self)
        self._pulse_period_1_tool_bar.addWidget(Qt.QLabel('Signal 1 Period (s)'+": "))
        self._pulse_period_1_line_edit = Qt.QLineEdit(str(self.pulse_period_1))
        self._pulse_period_1_tool_bar.addWidget(self._pulse_period_1_line_edit)
        self._pulse_period_1_line_edit.returnPressed.connect(
        	lambda: self.set_pulse_period_1(eng_notation.str_to_num(str(self._pulse_period_1_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._pulse_period_1_tool_bar)
        self._pulse_period_0_tool_bar = Qt.QToolBar(self)
        self._pulse_period_0_tool_bar.addWidget(Qt.QLabel('Signal 0 Period (s)'+": "))
        self._pulse_period_0_line_edit = Qt.QLineEdit(str(self.pulse_period_0))
        self._pulse_period_0_tool_bar.addWidget(self._pulse_period_0_line_edit)
        self._pulse_period_0_line_edit.returnPressed.connect(
        	lambda: self.set_pulse_period_0(eng_notation.str_to_num(str(self._pulse_period_0_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._pulse_period_0_tool_bar)
        self._pulse_duty_1_range = Range(0, 1, 0.001, 0.2, 200)
        self._pulse_duty_1_win = RangeWidget(self._pulse_duty_1_range, self.set_pulse_duty_1, 'Signal 1 Duty', "counter_slider", float)
        self.top_layout.addWidget(self._pulse_duty_1_win)
        self._pulse_duty_0_range = Range(0, 1, 0.001, 0.2, 200)
        self._pulse_duty_0_win = RangeWidget(self._pulse_duty_0_range, self.set_pulse_duty_0, 'Signal 0 Duty', "counter_slider", float)
        self.top_layout.addWidget(self._pulse_duty_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(network_decim, firdes.low_pass(
        	1, receiver_samp_rate, receiver_samp_rate / network_decim / 2, 1000, firdes.WIN_RECTANGULAR, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(2, (20, ), 24000, receiver_samp_rate)
        self.blocks_vector_source_x_0_1 = blocks.vector_source_c([1]*pulse_duty_ticks_1 + [0]*(pulse_period_ticks_1-pulse_duty_ticks_1), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c([1]*pulse_duty_ticks_0 + [0]*(pulse_period_ticks_0-pulse_duty_ticks_0), True, 1, [])
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1024, 'localhost', 39253, 1472, True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_gr_complex*1, receiver_samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, receiver_samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_repeat_0_1 = blocks.repeat(gr.sizeof_gr_complex*1, receiver_samp_rate / pulse_samp_rate)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, receiver_samp_rate / pulse_samp_rate)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.002, ))
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((direction_1, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((direction_0, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(receiver_samp_rate, analog.GR_COS_WAVE, freq_1 - tuner_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(receiver_samp_rate, analog.GR_COS_WAVE, freq_0 - tuner_freq, 1, 0)
        self.analog_noise_source_x_1 = analog.noise_source_c(analog.GR_UNIFORM, noise_correction_factor/2**n_adc_bits, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_correction_factor/10**(SNR/20), 0)
        self.DirectionalAntenna_1 = DirectionalAntenna_1.blk(pattern_file_name="/home/chris/Documents/GVSU/Capstone/GNU Radio/rad_pattern.csv", use_degrees=True, mirror=True)
        self.DirectionalAntenna = DirectionalAntenna.blk(pattern_file_name="/home/chris/Documents/GVSU/Capstone/GNU Radio/rad_pattern.csv", use_degrees=True, mirror=True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.DirectionalAntenna, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.DirectionalAntenna_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.DirectionalAntenna, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.DirectionalAntenna_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.DirectionalAntenna, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.DirectionalAntenna_1, 1))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_repeat_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.blocks_repeat_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.udp_repeat_source, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.udp_repeat_source, 0), (self.blocks_add_const_vxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pulse_samp_rate(self):
        return self.pulse_samp_rate

    def set_pulse_samp_rate(self, pulse_samp_rate):
        self.pulse_samp_rate = pulse_samp_rate
        self.set_pulse_period_ticks_1(int(math.ceil(self.pulse_period_1 * self.pulse_samp_rate)))
        self.set_pulse_period_ticks_0(int(math.ceil(self.pulse_period_0 * self.pulse_samp_rate)))
        self.blocks_repeat_0_1.set_interpolation(self.receiver_samp_rate / self.pulse_samp_rate)
        self.blocks_repeat_0.set_interpolation(self.receiver_samp_rate / self.pulse_samp_rate)

    def get_pulse_period_1(self):
        return self.pulse_period_1

    def set_pulse_period_1(self, pulse_period_1):
        self.pulse_period_1 = pulse_period_1
        self.set_pulse_period_ticks_1(int(math.ceil(self.pulse_period_1 * self.pulse_samp_rate)))
        Qt.QMetaObject.invokeMethod(self._pulse_period_1_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pulse_period_1)))

    def get_pulse_period_0(self):
        return self.pulse_period_0

    def set_pulse_period_0(self, pulse_period_0):
        self.pulse_period_0 = pulse_period_0
        self.set_pulse_period_ticks_0(int(math.ceil(self.pulse_period_0 * self.pulse_samp_rate)))
        Qt.QMetaObject.invokeMethod(self._pulse_period_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pulse_period_0)))

    def get_pulse_period_ticks_1(self):
        return self.pulse_period_ticks_1

    def set_pulse_period_ticks_1(self, pulse_period_ticks_1):
        self.pulse_period_ticks_1 = pulse_period_ticks_1
        self.set_pulse_duty_ticks_1(int(math.floor(self.pulse_duty_1 * self.pulse_period_ticks_1)))
        self.blocks_vector_source_x_0_1.set_data([1]*self.pulse_duty_ticks_1 + [0]*(self.pulse_period_ticks_1-self.pulse_duty_ticks_1), [])

    def get_pulse_period_ticks_0(self):
        return self.pulse_period_ticks_0

    def set_pulse_period_ticks_0(self, pulse_period_ticks_0):
        self.pulse_period_ticks_0 = pulse_period_ticks_0
        self.set_pulse_duty_ticks_0(int(math.floor(self.pulse_duty_0 * self.pulse_period_ticks_0)))
        self.blocks_vector_source_x_0.set_data([1]*self.pulse_duty_ticks_0 + [0]*(self.pulse_period_ticks_0-self.pulse_duty_ticks_0), [])

    def get_pulse_duty_1(self):
        return self.pulse_duty_1

    def set_pulse_duty_1(self, pulse_duty_1):
        self.pulse_duty_1 = pulse_duty_1
        self.set_pulse_duty_ticks_1(int(math.floor(self.pulse_duty_1 * self.pulse_period_ticks_1)))

    def get_pulse_duty_0(self):
        return self.pulse_duty_0

    def set_pulse_duty_0(self, pulse_duty_0):
        self.pulse_duty_0 = pulse_duty_0
        self.set_pulse_duty_ticks_0(int(math.floor(self.pulse_duty_0 * self.pulse_period_ticks_0)))

    def get_tuner_freq(self):
        return self.tuner_freq

    def set_tuner_freq(self, tuner_freq):
        self.tuner_freq = tuner_freq
        self.qtgui_sink_x_1.set_frequency_range(self.tuner_freq, self.receiver_samp_rate / self.network_decim)
        self.analog_sig_source_x_0_1.set_frequency(self.freq_1 - self.tuner_freq)
        self.analog_sig_source_x_0.set_frequency(self.freq_0 - self.tuner_freq)

    def get_receiver_samp_rate(self):
        return self.receiver_samp_rate

    def set_receiver_samp_rate(self, receiver_samp_rate):
        self.receiver_samp_rate = receiver_samp_rate
        self.qtgui_sink_x_1.set_frequency_range(self.tuner_freq, self.receiver_samp_rate / self.network_decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.receiver_samp_rate, self.receiver_samp_rate / self.network_decim / 2, 1000, firdes.WIN_RECTANGULAR, 6.76))
        self.blocks_throttle_0_1.set_sample_rate(self.receiver_samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.receiver_samp_rate)
        self.blocks_repeat_0_1.set_interpolation(self.receiver_samp_rate / self.pulse_samp_rate)
        self.blocks_repeat_0.set_interpolation(self.receiver_samp_rate / self.pulse_samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.receiver_samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.receiver_samp_rate)

    def get_pulse_samp_rate_1(self):
        return self.pulse_samp_rate_1

    def set_pulse_samp_rate_1(self, pulse_samp_rate_1):
        self.pulse_samp_rate_1 = pulse_samp_rate_1

    def get_pulse_duty_ticks_1(self):
        return self.pulse_duty_ticks_1

    def set_pulse_duty_ticks_1(self, pulse_duty_ticks_1):
        self.pulse_duty_ticks_1 = pulse_duty_ticks_1
        self.blocks_vector_source_x_0_1.set_data([1]*self.pulse_duty_ticks_1 + [0]*(self.pulse_period_ticks_1-self.pulse_duty_ticks_1), [])

    def get_pulse_duty_ticks_0(self):
        return self.pulse_duty_ticks_0

    def set_pulse_duty_ticks_0(self, pulse_duty_ticks_0):
        self.pulse_duty_ticks_0 = pulse_duty_ticks_0
        self.blocks_vector_source_x_0.set_data([1]*self.pulse_duty_ticks_0 + [0]*(self.pulse_period_ticks_0-self.pulse_duty_ticks_0), [])

    def get_noise_correction_factor(self):
        return self.noise_correction_factor

    def set_noise_correction_factor(self, noise_correction_factor):
        self.noise_correction_factor = noise_correction_factor
        self.analog_noise_source_x_1.set_amplitude(self.noise_correction_factor/2**self.n_adc_bits)
        self.analog_noise_source_x_0.set_amplitude(self.noise_correction_factor/10**(self.SNR/20))

    def get_network_decim(self):
        return self.network_decim

    def set_network_decim(self, network_decim):
        self.network_decim = network_decim
        self.qtgui_sink_x_1.set_frequency_range(self.tuner_freq, self.receiver_samp_rate / self.network_decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.receiver_samp_rate, self.receiver_samp_rate / self.network_decim / 2, 1000, firdes.WIN_RECTANGULAR, 6.76))

    def get_n_adc_bits(self):
        return self.n_adc_bits

    def set_n_adc_bits(self, n_adc_bits):
        self.n_adc_bits = n_adc_bits
        self.analog_noise_source_x_1.set_amplitude(self.noise_correction_factor/2**self.n_adc_bits)

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.analog_sig_source_x_0_1.set_frequency(self.freq_1 - self.tuner_freq)

    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.analog_sig_source_x_0.set_frequency(self.freq_0 - self.tuner_freq)

    def get_direction_1(self):
        return self.direction_1

    def set_direction_1(self, direction_1):
        self.direction_1 = direction_1
        self.blocks_add_const_vxx_1.set_k((self.direction_1, ))

    def get_direction_0(self):
        return self.direction_0

    def set_direction_0(self, direction_0):
        self.direction_0 = direction_0
        self.blocks_add_const_vxx_0.set_k((self.direction_0, ))

    def get_SNR(self):
        return self.SNR

    def set_SNR(self, SNR):
        self.SNR = SNR
        self.analog_noise_source_x_0.set_amplitude(self.noise_correction_factor/10**(self.SNR/20))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
