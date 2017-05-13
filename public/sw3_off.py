# Edit line 6 to match your chosen GPIO pin-off
import logging
#import RPi.GPIO as GPIO

logging.warning('3gpio pin toggle OFF!')  # will print a message to the console

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN)
#GPIO.cleanup()

#!/usr/bin/env python

import serial

ser = serial.Serial(
        port='/dev/serial0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

print "Serial is open: " + str(ser.isOpen())

print "Now Writing"
ser.write("q")
#ser.write("AT+CONNL")
print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

ser.close()
