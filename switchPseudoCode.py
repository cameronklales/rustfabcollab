#pseudo code for switch

#main function
    # enable ISRs
    # set reset switch for relay pin to high (blocked by switch)
    # set relay power to hight
    # set relay trigger to low
    # set relay 
    # enable RFID reader

#ISR(Pinchange interrupt for RFID)
    #get chip value
    #store chip value
    #check chip value against others
#pseudo code for switch

#main function
    # enable ISRs
    # set reset switch for relay pin to high (blocked by switch)
    # set relay power to hight
    # set relay trigger to low
    # set relay 
    # enable RFID reader

#ISR(Pinchange interrupt for RFID)
    #get chip value
    #store chip value
    #check chip value against others
#ISR(switch)
#read pin value of on/off
    #if off AND rfid = pass
       #fire relay switch
     # if on
      #turn off relay switch
