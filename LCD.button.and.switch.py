from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import board
from digitalio import DigitalInOut, Direction, Pull


button = DigitalInOut(board.D8)
button.direction = Direction.INPUT
button.pull = Pull.UP

switch = DigitalInOut(board.D10)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.S
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
# sets up LCD, tells how many rows and columns it has 

lcd.set_cursor_pos(1,4) # tells LCD where to start printing
lcd.print("button presses") # what to print 
lcd.clear() # clear LCD after 

counter = 0  # to count the number of button presses, sets at zero to begin

now = True
later = True
switchValue = True
# establishes variables, sets all to True for the while True 
while True:
    now = button.value # makes the value of the button (True, False) equal now, which is True 
    switchValue = switch.value
    print(str(switchValue)) # print on the LCD 
    if  now == False and later == True: 
        lcd.set_cursor_pos(0,0)
        lcd.print("pushed")
        lcd.set_cursor_pos (1,1)
        lcd.print(str(counter))
        time.sleep(0.05)
        lcd.print("  ")
        now = True
        # if now is false and later is true, the LCD screen should print "pushed" 
        if switchValue:
            counter += 1
        if not switchValue:
            counter -= 1

    later = button.value
    time.sleep(0.05)