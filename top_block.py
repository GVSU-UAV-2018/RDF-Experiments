#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Apr  7 09:17:12 2018
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
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import DirectionalAntenna
import collar_detect
import math
import scipy
import sip
import sys
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
        self.pulse_period = pulse_period = 1
        self.pulse_period_ticks = pulse_period_ticks = int(math.ceil(pulse_period * pulse_samp_rate))
        self.pulse_duty = pulse_duty = 0.2
        self.variable_0 = variable_0 = 0
        self.tuner_freq = tuner_freq = 150000000
        self.receiver_samp_rate = receiver_samp_rate = 6000000
        self.pulse_duty_ticks = pulse_duty_ticks = int(math.floor(pulse_duty * pulse_period_ticks))
        self.freq = freq = 150000000
        self.display_scale = display_scale = 0
        self.direction = direction = 0
        self.SNR = SNR = 50

        ##################################################
        # Blocks
        ##################################################
        self._tuner_freq_range = Range(148000000, 152000000, 1, 150000000, 200)
        self._tuner_freq_win = RangeWidget(self._tuner_freq_range, self.set_tuner_freq, "tuner_freq", "counter_slider", float)
        self.top_layout.addWidget(self._tuner_freq_win)
        self._freq_range = Range(148000000, 152000000, 100000, 150000000, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Freq', "counter_slider", float)
        self.top_layout.addWidget(self._freq_win)
        self._display_scale_range = Range(0, 100, 1, 0, 200)
        self._display_scale_win = RangeWidget(self._display_scale_range, self.set_display_scale, "display_scale", "dial", float)
        self.top_layout.addWidget(self._display_scale_win)
        self._direction_range = Range(0, 360, 1, 0, 1)
        self._direction_win = RangeWidget(self._direction_range, self.set_direction, 'Direction', "counter_slider", float)
        self.top_layout.addWidget(self._direction_win)
        self._SNR_range = Range(0, 100, 1, 50, 200)
        self._SNR_win = RangeWidget(self._SNR_range, self.set_SNR, "SNR", "counter_slider", float)
        self.top_layout.addWidget(self._SNR_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            512,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0, 10**(display_scale/10))
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	tuner_freq, #fc
        	receiver_samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(True)



        self._pulse_period_tool_bar = Qt.QToolBar(self)
        self._pulse_period_tool_bar.addWidget(Qt.QLabel('Pulse period (s)'+": "))
        self._pulse_period_line_edit = Qt.QLineEdit(str(self.pulse_period))
        self._pulse_period_tool_bar.addWidget(self._pulse_period_line_edit)
        self._pulse_period_line_edit.returnPressed.connect(
        	lambda: self.set_pulse_period(eng_notation.str_to_num(str(self._pulse_period_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._pulse_period_tool_bar)
        self._pulse_duty_range = Range(0, 1, 0.001, 0.2, 200)
        self._pulse_duty_win = RangeWidget(self._pulse_duty_range, self.set_pulse_duty, "pulse_duty", "counter_slider", float)
        self.top_layout.addWidget(self._pulse_duty_win)
        self.fft_vxx_0 = fft.fft_vfc(512, True, (window.rectangular(512)), 1)
        self.collar_detect = collar_detect.collar_detect()
        self.channels_quantizer_0_0 = channels.quantizer(10)
        self.channels_quantizer_0 = channels.quantizer(10)
        self.blocks_vector_source_x_0 = blocks.vector_source_c([1]*pulse_duty_ticks + [0]*(pulse_period_ticks-pulse_duty_ticks), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, receiver_samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_cc(1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, 512)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, receiver_samp_rate / pulse_samp_rate)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(512)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(512)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(receiver_samp_rate, analog.GR_COS_WAVE, freq - tuner_freq, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 30/10**(SNR/20), 0)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 8192)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, direction)
        self.DirectionalAntenna = DirectionalAntenna.blk(pattern_file_name="/home/chris/Documents/GVSU/Capstone/GNU Radio/rad_pattern.csv", use_degrees=True, mirror=True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.DirectionalAntenna, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.DirectionalAntenna, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.channels_quantizer_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.channels_quantizer_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.collar_detect, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.DirectionalAntenna, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.channels_quantizer_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.channels_quantizer_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_xx_1, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pulse_samp_rate(self):
        return self.pulse_samp_rate

    def set_pulse_samp_rate(self, pulse_samp_rate):
        self.pulse_samp_rate = pulse_samp_rate
        self.set_pulse_period_ticks(int(math.ceil(self.pulse_period * self.pulse_samp_rate)))
        self.blocks_repeat_0.set_interpolation(self.receiver_samp_rate / self.pulse_samp_rate)

    def get_pulse_period(self):
        return self.pulse_period

    def set_pulse_period(self, pulse_period):
        self.pulse_period = pulse_period
        self.set_pulse_period_ticks(int(math.ceil(self.pulse_period * self.pulse_samp_rate)))
        Qt.QMetaObject.invokeMethod(self._pulse_period_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pulse_period)))

    def get_pulse_period_ticks(self):
        return self.pulse_period_ticks

    def set_pulse_period_ticks(self, pulse_period_ticks):
        self.pulse_period_ticks = pulse_period_ticks
        self.set_pulse_duty_ticks(int(math.floor(self.pulse_duty * self.pulse_period_ticks)))
        self.blocks_vector_source_x_0.set_data([1]*self.pulse_duty_ticks + [0]*(self.pulse_period_ticks-self.pulse_duty_ticks), [])

    def get_pulse_duty(self):
        return self.pulse_duty

    def set_pulse_duty(self, pulse_duty):
        self.pulse_duty = pulse_duty
        self.set_pulse_duty_ticks(int(math.floor(self.pulse_duty * self.pulse_period_ticks)))

    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_tuner_freq(self):
        return self.tuner_freq

    def set_tuner_freq(self, tuner_freq):
        self.tuner_freq = tuner_freq
        self.qtgui_sink_x_0.set_frequency_range(self.tuner_freq, self.receiver_samp_rate)
        self.analog_sig_source_x_0.set_frequency(self.freq - self.tuner_freq)

    def get_receiver_samp_rate(self):
        return self.receiver_samp_rate

    def set_receiver_samp_rate(self, receiver_samp_rate):
        self.receiver_samp_rate = receiver_samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.tuner_freq, self.receiver_samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.receiver_samp_rate)
        self.blocks_repeat_0.set_interpolation(self.receiver_samp_rate / self.pulse_samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.receiver_samp_rate)

    def get_pulse_duty_ticks(self):
        return self.pulse_duty_ticks

    def set_pulse_duty_ticks(self, pulse_duty_ticks):
        self.pulse_duty_ticks = pulse_duty_ticks
        self.blocks_vector_source_x_0.set_data([1]*self.pulse_duty_ticks + [0]*(self.pulse_period_ticks-self.pulse_duty_ticks), [])

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq - self.tuner_freq)

    def get_display_scale(self):
        return self.display_scale

    def set_display_scale(self, display_scale):
        self.display_scale = display_scale
        self.qtgui_vector_sink_f_0.set_y_axis(0, 10**(self.display_scale/10))

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction
        self.analog_const_source_x_0.set_offset(self.direction)

    def get_SNR(self):
        return self.SNR

    def set_SNR(self, SNR):
        self.SNR = SNR
        self.analog_noise_source_x_0.set_amplitude(30/10**(self.SNR/20))


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
