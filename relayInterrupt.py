import binascii
import sys
import Adafruit_PN532 as PN532
import time
import RPi.GPIO as GPIO


#board setup
GPIO.setmode(GPIO.BCM)

#declare variables for pins
pulsepin = 7 #relay output pin
testpin = 8
pingpin = 17
pingpin2 = 27 #interrupt pin
onOff =1 #true = off false = on

#pin setup
GPIO.setup(pulsepin, GPIO.OUT)
GPIO.setup(testpin, GPIO.OUT) 
GPIO.setup(pingpin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pingpin2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def pinup(gopin):
    GPIO.output(gopin, True) ## Turn on GPIO pin 7
def pindown(gopin):
    GPIO.output(gopin, False) ## Turn on GPIO pin 7'
def my_callback(channel):  
    print "falling edge detected on 17"
    pindown(pulsepin)
def my_callback2
(channel):  
    print "falling edge detected on 27"
    pinup(pulsepin)

pinup(pulsepin)
#interrupt on pingpin
GPIO.add_event_detect(pingpin, GPIO.FALLING, callback= my_callback, bouncetime=300) 
GPIO.add_event_detect(pingpin2, GPIO.FALLING, callback= my_callback2, bouncetime=300)
#try statment for some reason
try:  
    print ("Waiting for rising edge on port 24")  
    GPIO.wait_for_edge(24, GPIO.RISING)  
    print ("Rising edge detected on port 24. Here endeth the third lesson.")   
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()          # clean up GPIO on normal exit  
