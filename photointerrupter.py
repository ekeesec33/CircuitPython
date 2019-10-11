import board
from digitalio import DigitalInOut, Direction, Pull
import time

button = DigitalInOut (board.D7)
button.direction = Direction.INPUT # is an input because we are finding the output of the number of counts 
button.pull = Pull.UP #pulls the button up in order to 
now = True
later = True
# establishes "now" and "later" as variables 
lastTime = 0 # this is set to 0 becuase it'll go with the counter
counter = 0

while True:
    #print(button.value)
    #time.sleep(.1)
    nowT = time.monotonic() # another variable, but only while "x" is true 
    now = button.value

    if nowT - 4 >= lastTime: 
        print("interrupted")
        print(counter)
        #time.sleep(.05)
        lastTime = time.monotonic() # time.monotonic is a delay that returns seconds, not milliseconds
    # if nowT (time.monotonic) minus 4 is greater than or equal to lastTime then...
    # above comment is a true statement becuase lastTime is 0
    # nowT = the amount of time since you have last been interrupted
    if now == False and later == True: # below is the code for counting how many times the photointerrupter has been interrupted
        counter += 1
       #print(counter)
    #time.sleep(0.05)
    later = now


#monotonic