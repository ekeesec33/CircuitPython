import board
from digitalio import DigitalInOut, Direction, Pull
import time

button = DigitalInOut (board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP
now = True
later = True
lastTime = 0
counter = 0
while True:
    nowT = time.monotonic()
    now = button.value
    if now == False and later == True:
        #if interrupted:
        if nowT - 4 >= lastTime:
            counter += 1
            print("interrupted")
            print(str(counter))
            time.sleep(.05)
            lastTime = time.monotonic

    if now == False and later == True:
        print("off")
        time.sleep(0.05)
        now = True
        time.monotonic