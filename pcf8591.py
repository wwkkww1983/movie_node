#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
while True:
    bus.write_byte(address, A0)
    value0 = bus.read_byte(address)
    time.sleep(0.1)
    bus.write_byte(address, A1)
    value1 = bus.read_byte(address)
    time.sleep(0.1)
    bus.write_byte(address, A2)
    value2 = bus.read_byte(address)
    time.sleep(0.1)
    bus.write_byte(address, A3)
    value3 = bus.read_byte(address)
    time.sleep(0.1)
    print ("%1.3f")%(value0 * 3.3 / 255),("%1.3f")%(value1 * 3.3 / 255),("%1.3f")%(value2 * 3.3 / 255),("%1.3f")%(value3 * 3.3 / 255)