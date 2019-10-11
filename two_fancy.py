import board #pylint:disable-msg=import-error
import digitalio #pylint:disable-msg=import-error
from fancyLED import FancyLED # calling fancyLED class from fancyLED

K1 = board.D1
J1 = board.D5
L1 = board.D12
K2 = board.D9
J2 = board.D7
L2 = board.D4
# gives each value a pin 
fancy1 = FancyLED (K1,J1,L1) # using pins from one of the tri-color LEDs, and not the other 
fancy2 = FancyLED (K2,J2,L2)

while True: # in fancyLED, goes to the according section and follows that code
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()
