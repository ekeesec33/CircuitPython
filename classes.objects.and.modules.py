# the purpose of this assignment was to teach us how to use "subsitution" in code. 
# basically it's as if you say "2x = 10" and you know that 5 = x, then you are able to subsitute 5 in for x in your original equation.
# in this code, RGB is the "x"

from rgb import RGB   # import the RGB class from the rgb module
import board
import time

#below sets up pins for each of the LEDs
r1 = board.D2
g1 = board.D3
b1 = board.D4

r2 = board.D5
g2 = board.D7
b2 = board.D1


myRGB1 = RGB(r1,g1,b1)   # create a new RGB object, using pins 2, 3, and 4
myRGB2 = RGB(r2,g2,b2)   # create a new RGB object, using pins 5, 1, and 7

myRGB1.change_pins(r1,g1,b1)
print(myRGB1.kind)
print(myRGB2.kind)
myRGB1.change_name("rex")
print(myRGB1.name)

myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Glow... you get it...
time.sleep(1)
myRGB1.magenta()      # Did you know magenta isn't in the rainbow?
myRGB2.yellow()       # Like you learned in first grade, red and green make... huh?
time.sleep(1)
# extra spicy (optional) part
myRGB1.rainbow() # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
#myRGB2.rainbow() # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
#time.sleep(1)

# in the above code, I used the different LED colors to mix and match in order to make new ones. 