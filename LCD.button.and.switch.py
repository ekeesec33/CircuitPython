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


lcd.set_cursor_pos(1,4)
lcd.print("button presses")
lcd.clear()

counter = 0

now = True
later = True
switchValue = True
while True:
    now = button.value
    switchValue = switch.value
    print(str(switchValue))
    if  now == False and later == True:
        lcd.set_cursor_pos(0,0)
        lcd.print("pushed")
        lcd.set_cursor_pos (1,1)
        lcd.print(str(counter))
        time.sleep(0.05)
        lcd.print("  ")
        now = True
        if switchValue:
            counter += 1
        if not switchValue:
            counter -= 1

    later = button.value
    time.sleep(0.05)