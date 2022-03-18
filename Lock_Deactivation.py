Import RPi.GPIO as GPIO 
Import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.LOW)
Time.sleep(1)
GPIO.cleanup()
#This is an emergency close function just incase you needed to close the door before the set time loop in the other open and close code which would be used casually.
#This code will run when the used Exclamation mark button is used.
