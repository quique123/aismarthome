# Edit line 6 to match your chosen GPIO pin-on
import logging
#import RPi.GPIO as GPIO

logging.warning('gpio pin toggle!')  # will print a message to the console

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.OUT)

## TEMP CALL togglerelay.py file's code snippet
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
ser.write("h")
#ser.write("AT+CONNL")
print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

ser.close()
