import time
import signal
import atexit
import RPi.GPIO as GPIO
import smbus

atexit.register(GPIO.cleanup)

horizon_servopin = 12
vertical_servopin = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(horizon_servopin, GPIO.OUT, initial=False)
GPIO.setup(vertical_servopin, GPIO.OUT, initial=False)
p_horizon = GPIO.PWM(horizon_servopin, 50)
p_vertical = GPIO.PWM(vertical_servopin, 50)
p_horizon.start(0)
p_vertical.start(0)


def servodriver(servo, angle):
    i = angle / 3.6 + 25
    servo.ChangeDutyCycle(i / 10.0)


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


horizon_light_min_channel = A0
horizon_light_max_channel = A1
vertical_light_min_channel = A2
vertical_light_max_channel = A3
light_gap = 10
horizon_angle = 0
vertical_angle = 0
delay_time = 0.01
max_angle = 360
min_angle = -5

'''
while True:
	horizon_light_min = read_channel(horizon_light_min_channel)
	horizon_light_max = read_channel(horizon_light_max_channel)
	vertical_light_min = read_channel(vertical_light_min_channel)
	vertical_light_max = read_channel(vertical_light_max_channel)
	print horizon_light_min, horizon_light_max, vertical_light_min, vertical_light_max
'''

while True:
    horizon_light_min = read_channel(horizon_light_min_channel)
    horizon_light_max = read_channel(horizon_light_max_channel)
    vertical_light_min = read_channel(vertical_light_min_channel)
    vertical_light_max = read_channel(vertical_light_max_channel)
    while horizon_light_max - horizon_light_min > light_gap:
        if horizon_angle + 1 > max_angle:
            break
        else:
            horizon_angle = horizon_angle + 1
        servodriver(p_horizon, horizon_angle)
        time.sleep(delay_time)
        print horizon_light_min, horizon_light_max, vertical_light_min, vertical_light_max, horizon_angle, vertical_angle
        horizon_light_min = read_channel(horizon_light_min_channel)
        horizon_light_max = read_channel(horizon_light_max_channel)
    while horizon_light_min - horizon_light_max > light_gap:
        if horizon_angle - 1 < min_angle:
            break
        else:
            horizon_angle = horizon_angle - 1
        servodriver(p_horizon, horizon_angle)
        time.sleep(delay_time)
        print horizon_light_min, horizon_light_max, vertical_light_min, vertical_light_max, horizon_angle, vertical_angle
        horizon_light_min = read_channel(horizon_light_min_channel)
        horizon_light_max = read_channel(horizon_light_max_channel)
    while vertical_light_max - vertical_light_min > light_gap:
        if vertical_angle + 1 > max_angle:
            break
        else:
            vertical_angle = vertical_angle + 1
        servodriver(p_vertical, vertical_angle)
        time.sleep(delay_time)
        print horizon_light_min, horizon_light_max, vertical_light_min, vertical_light_max, horizon_angle, vertical_angle
        vertical_light_min = read_channel(vertical_light_min_channel)
        vertical_light_max = read_channel(vertical_light_max_channel)
    while vertical_light_min - vertical_light_max > light_gap:
        if vertical_angle - 1 < min_angle:
            break
        else:
            vertical_angle = vertical_angle - 1
        servodriver(p_vertical, vertical_angle)
        time.sleep(delay_time)
        print horizon_light_min, horizon_light_max, vertical_light_min, vertical_light_max, horizon_angle, vertical_angle
        vertical_light_min = read_channel(vertical_light_min_channel)
        vertical_light_max = read_channel(vertical_light_max_channel)

'''
#for i in range(25,125,1):
for i in range(0,181,2):
	servodriver(p_horizon,i)
	servodriver(p_vertical,i/2.0)
	print i
	time.sleep(0.5)
'''
'''
while(True):
  for i in range(0,360,10):
      p.ChangeDutyCycle(12.5-5*i/360)
      time.sleep(1)
  for i in  range(0,360,10):
       p.ChangeDutyCycle(7.5-5*i/360)
       time.sleep(1)
'''
