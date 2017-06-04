def pinup(gopin):
    GPIO.setup(gopin, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(gopin, True) ## Turn on GPIO pin 7
def pindown(gopin):
    GPIO.setup(gopin, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(gopin, False) ## Turn on GPIO pin 7'
try:  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    print "\nFalling edge detected. Now your program can continue with"  
    print "whatever was waiting for a button press."  
