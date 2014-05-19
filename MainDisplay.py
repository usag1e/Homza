import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD )

# ISS
GPIO.setup( 3, GPIO.OUT )
# Weather
GPIO.setup( 7, GPIO.OUT )
# Transportation
GPIO.setup( 9, GPIO.OUT )
# Internet
GPIO.setup( 11, GPIO.OUT )

# Check infos in the DB regularly

# Clean
GPIO.cleanup()
