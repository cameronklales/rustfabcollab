import binascii
import sys
import Adafruit_PN532 as PN532
import time
import RPi.GPIO as GPIO

# Configuration for a Raspberry Pi:
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

#.hexlify

#tData = file('tData.txt')
#dataList=[]

#for a in tData:
    #tData.format(binascii(tData))
    #dataList[a]
    
#dataList.sort()

#board setup
GPIO.setmode(GPIO.BCM)

# Create an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)

# Call begin to initialize communication with the PN532.  Must be done before
# any other calls to the PN532!
pn532.begin()

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

#declare variables for pins
pulsepin = 17 #relay output pin
testpin = 27
pingpin = 17
pingpin2 = 27 #interrupt pin
onOff =1 #true = off false = on

#pin setup
#GPIO.setup(pulsepin, GPIO.OUT)
GPIO.setup(testpin, GPIO.OUT) 
GPIO.setup(pulsepin,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def pinup(gopin):
    GPIO.output(gopin, True) ## Turn on GPIO pin 7
def pindown(gopin):
    GPIO.output(gopin, False) ## Turn on GPIO pin 7'
def my_callback(channel):  
    print "falling edge detected on 17"
    pindown(testpin)
#def my_callback2(channel):  
   #print "falling edge detected on 27"
    #pinup(pulsepin)

GPIO.add_event_detect(pulsepin, GPIO.FALLING, callback= my_callback, bouncetime=300)
#UserData=card number
    #dataList = temples list of accepted card ID's
while True:
    
    userData = pn532.read_passive_target()
    if userData is None:
        print ("No card found.")
        continue
    if not userData is None:
        print("Card found")
        pinup(testpin)
    print("Card number "+userData)
    
    #if userData in dataList:
        #print("Card accepted")




#interrupt on pingpin

#GPIO.add_event_detect(pingpin2, GPIO.FALLING, callback= my_callback2, bouncetime=300)
#try statment for some reason
##try:  
##    print ("Waiting for rising edge on port 24")  
##    GPIO.wait_for_edge(24, GPIO.RISING)  
##    print ("Rising edge detected on port 24. Here endeth the third lesson.")   
##except KeyboardInterrupt:  
##    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
##GPIO.cleanup()          # clean up GPIO on normal exit  
