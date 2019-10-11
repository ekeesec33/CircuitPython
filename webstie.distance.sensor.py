import time
import board
import busio
import neopixel
import adafruit_hcsr04
from simpleio import map_range

TRIGGER_DISTANCE = 500          # number of mm where the light toggles
NEOPIXEL_PIN = board.NEOPIXEL
NUMBER_OF_PIXELS = 1


#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_vl53l0x.VL53L0X(i2c)
sensor = adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D10)



#for i in range(NUMBER_OF_PIXELS):
    #strip[i] = (0, 0, 0)
    #strip.show()
    #time.sleep(0.1)
    #strip[i] = (0, 0, 0)
   # strip.show()
dot = neopixel.NeoPixel(board.NEOPIXEL, 1) # establishes the neopixel on the metro as a "dot"
dot(0) = (10, 0, 0) # for r, g, and b, is each an interval, here r is 10 

while True:
    try:
        distnace = sonar.distance
        print(distance) # printing the sonar distnace
        if sonar.distance < 20: # when the distance is less than 20, red is on
            r = map_range(distance, 5,20,255,0)
            b = map_range(distance, 5,20,0,255)
            dot.fill((10,0,0))
            print("red")
        else: # if the distance is greater than 20, blue "fades" into green
            b = map(val,20,35,255,0)
            g = map(val,20,35,0,255)
            #dot.fill((int(r), int(b), int(g)))
            dot.fill((0,0,10))
            time.sleep(.01)
            print("green")
    #dot.fill((int(r), int(b), int(g)))

    except:
        print("out of range") # none of these distances, print out of range

    #time.sleep(0.05)