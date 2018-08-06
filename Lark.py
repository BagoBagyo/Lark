# K,R,G,Y,B,W

import time
count = int(0)

try:
	import RPi.GPIO as GPIO
	print(GPIO.VERSION)
except RuntimeError:
	print("Error importing PRi.GPIO!")

# Helper function to convert fret 1-23 to GPIO pin
def fret2Pin(fret):
        fret2Pin = [0,8,7,11,13,15,19,21,23,29,31,33,35,37,40,38,36,16,26,24,22,18]
        
        return fret2Pin[fret]
 
# Helper function to convert GPIO pin 1-40 to fret 1-23
def Pin2Fret(Pin):
        Pin2Fret = [0,0,0,0,0,0,0,2,1,0,0,3,23,4,0,5,17,0,21,6,0,7,20,8,19,0,0,0,0,9,0,10,0,11,0,12,16,13,15,0,14]
        return Pin2Fret[Pin]
 
# ISR when frets get shorted by string
def my_callback(pin):
        global count
        count+=1
        print('\nPin: {}, Fret: {}'.format(pin, Pin2Fret(pin)))
        #GPIO.output(STRING, 1)
        #GPIO.output(STRING, 0)

try:
        # Setup input pins
        GPIO.setmode(GPIO.BOARD)
        for fret in range(1, 22):
                #print("hello")
                print ("Fret: {}, Pin: {}".format(fret, fret2Pin(fret)))
                GPIO.setup(fret2Pin(fret), GPIO.IN, GPIO.PUD_UP)
                #GPIO.setup(fret2Pin(fret), GPIO.IN)
                #print(GPIO.gpio_function(fret2Pin(fret)))
                # Setup ISR
#                GPIO.add_event_detect(fret2Pin(fret), GPIO.FALLING, callback=my_callback)  # add falling edge detection on a channel
                GPIO.add_event_detect(fret2Pin(fret), GPIO.FALLING)  # add faling edge detection on a channel
        print()
        while True:
                #time.sleep(1)
                for fret in range(1,22):
                        if GPIO.event_detected(fret2Pin(fret)):
                                print("Fret: {}".format(fret
                                                        ))
                        #print("Count: {}".format(int(count/2)))
                #count=0
finally:
        GPIO.cleanup()
        print("Bye!")

