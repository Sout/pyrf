#!/usr/bin/env python

import sys
from pyrf.devices.thinkrf import WSA

# connect to wsa
dut = WSA()
dut.connect(sys.argv[1])

# setup test conditions
dut.reset()
dut.freq(2450e6)

print dut.peakfind()


