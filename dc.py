
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 19
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 2) 
pwm.start(0)


for i in range(100): #increase i to 100
  d = 100-i #defines d to decrease as i increases
  pwm.ChangeDutyCycle(d) #decreases duty cycle with d
  sleep(.02) 
pwm.stop() 