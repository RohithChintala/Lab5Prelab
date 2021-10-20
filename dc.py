
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 19
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)


for i in range(100): #increase i to 100
  d = 100-i #defines d to decrease as i increases
  pwm.ChangeDutyCycle(d) #decreases duty cycle with d
  sleep(.02) #sleeps for 5ms between duty cycle changes
pwm.stop() #stops pwm1