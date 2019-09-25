import time
import board
import busio
import neopixel
import adafruit_hcsr04
from simpleio import map_range

NEOPIXEL_PIN = board.NEOPIXEL
NUMBER_OF_PIXELS = 1


#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_vl53l0x.VL53L0X(i2c)
sensor = adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D10)
timeout = 10



#for i in range(NUMBER_OF_PIXELS):
    #strip[i] = (0, 0, 0)
    #strip.show()
    #time.sleep(0.1)
    #strip[i] = (0, 0, 0)
   # strip.show()
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    try:
        distance = sonar.distance
        print(distance)
        if sonar.distance < 20:
            r = map_range(distance, 0,20,255,0)
            b = map_range(distance, 5,20,0,255)
            g = map_range(distance,20,35,0,255)

            dot.fill((10,0,0))
            print("red")
        else:
            r = map_range(distance, 0,20,255,0)
            b = map_range(distance,20,35,255,0)
            g = map_range(distance,20,35,0,255)
            dot.fill((0,10,0))
            print("green")
        dot.fill((int(r), int(b), int(g)))
        time.sleep(.1)
    #dot.fill((int(r), int(b), int(g)))

    except:
        print("out of range")

    #time.sleep(0.05)