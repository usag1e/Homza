## Import GPIO library
import RPi.GPIO as GPIO 
## Import 'time' library. Allows us to use 'sleep'
import time 

## Use board pin numbering
GPIO.setmode(GPIO.BOARD)
## Setup GPIO Pin 7 to OUT
GPIO.setup(7, GPIO.OUT) 

##Define a function named Blink()
def Blink(numTimes,speed):
	## Run loop numTimes
	for i in range(0,numTimes):
		## Print current loop
		print "Iteration " + str(i+1)
		## Switch on pin 7
		GPIO.output(7,True)
		## Wait
		time.sleep(speed)
		## Switch off pin 7
		GPIO.output(7,False)
		## Wait
		time.sleep(speed)
	## When loop is complete, print "Done"
	print "Done" 
	GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))
