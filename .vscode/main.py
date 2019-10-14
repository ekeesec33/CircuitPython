import board #pylint:disable-msg=import-error
import digitalio #pylint:disable-msg=import-error
from fancyLED import fancyLED

K1 = board.D1
J1 = board.D5
L1 = board.D12
K2 = board.D9
J2 = board.D7
L2 = board.D4

fancy1 = FancyLED (K1,J1,L1)
fancy2 = FancyLED (K2,J2,L2)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()
