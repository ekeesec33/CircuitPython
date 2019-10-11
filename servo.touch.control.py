import time
import board
import pulseio # brings in pulse for servo
import touchio # brings in touch "sense" for wires
from adafruit_motor import servo


touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch = touchio.TouchIn
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
angle = 0
while True:
    my_servo.angle = angle
    if touch_A4.value:
        print ("Touched A4!")
        if angle < 180:
            angle += 1
        time.sleep(0.05)
    # if A4 is touched, and the angle of the servo is less than 180, add one to the angle and print "touched A4"
    if touch_A5.value:
        print("Touched A5!")
        if angle > 0:
            angle -= 1
    # if A5 is touched and the angle is greater than 0, subtract an angle from the servo and print "touched A5"
        time.sleep(0.05)