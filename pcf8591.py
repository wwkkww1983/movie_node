#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import time

address = 0x48
A0 = 0x01
A1 = 0x02
A2 = 0x03
A3 = 0x04
bus = smbus.SMBus(1)

def read_channel(A):
    bus.write_byte(address, A)
    value = bus.read_byte(address)
    return value

while True:
    value0 = read_channel(A0)
    value1 = read_channel(A1)
    value2 = read_channel(A2)
    value3 = read_channel(A3)
    print ("%1.3f")%(value0 * 3.3 / 255),("%1.3f")%(value1 * 3.3 / 255),("%1.3f")%(value2 * 3.3 / 255),("%1.3f")%(value3 * 3.3 / 255)
    time.sleep(0.1)