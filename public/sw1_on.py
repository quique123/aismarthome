# Edit line 6 to match your chosen GPIO pin
import logging
import RPi.GPIO as GPIO

logging.warning('gpio pin toggle!')  # will print a message to the console

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
