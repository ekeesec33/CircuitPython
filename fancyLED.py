import time  #pylint:disable-msg=import-error
import board  #pylint:disable-msg=import-error
import random #pylint:disable-msg=import-error
import digitalio #pylint:disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint:disable-msg=import-error
class FancyLED: # this is what is being called in for "x" in two_fancy
        def __init__(self, p1, p2, p3):
        print("you just made an object!")
        self.K1 = p1
        self.J1 = p2
        self.L1 = p3
# above gives each of the values a pin
        self.K1 = DigitalInOut(p1)
        self.K1.direction = Direction.OUTPUT # sets the direction of each value as an output becuase they are LEDs
        self.J1 = DigitalInOut(p2)
        self.J1.direction = Direction.OUTPUT
        self.L1 = DigitalInOut(p3)
        self.L1.direction = Direction.OUTPUT

   
    def alternate (self):
        #do alternate stuff
        print("alternate")
        self.K1.value = True
        self.J1.value = False
        self.L1.value = True
        # turns the first and third on, and the second off
        time.sleep(1)
        self.K1.value = False
        self.J1.value = True
        self.L1.value = False
        # turns the first and third off, and the second on
        time.sleep(1)
        self.J1.value = False
        self.K1.value = False
        # turns all off

    def blink (self):
        #do blink stuff
        print("blink")
        self.K1.value = True
        self.J1.value = True
        self.L1.value = True
        # turns all on
        time.sleep(0.5)
        self.K1.value = False
        self.J1.value = False
        self.L1.value = False
        # turns all off
        time.sleep(1)
    
    def chase (self):
        #do blink stuff
        print("chase")
        self.K1.value = True
        self.J1.value = False
        self.L1.value = False
        # turns the first off, and the second and third on
        time.sleep(0.05)
        self.K1.value = False
        self.J1.value = True
        self.L1.value = False
        # turns the first and third on, and the second off
        time.sleep(0.05)
        self.K1.value = False
        self.J1.value = False
        self.L1.value = True
        # turns the first and second on, and the third off
        time.sleep(1)
        self.L1.value = False
        # turns the third off

    def sparkle (self):
            for whatever in range (0,50):
                n = random.randint (0,3) # the range of n is 0 to 3, chosen randomly which one to go to
                print(n)
                if n == 0: # when n is 0, first is on, second and third are off
                    self.K1.value = False
                    self.J1.value = True
                    self.L1.value = True
                if n == 1: # when n is 1, first and third are off, second is on
                    self.K1.value = True
                    self.J1.value = False
                    self.L1.value = True
                if n == 2: # when n is 2, all are on
                    self.K1.value = True
                    self.J1.value = True
                    self.L1.value = True
                if n == 3: # when n is 3, first and second are on, third is off
                    self.K1.value = False
                    self.J1.value = False
                    self.L1.vaule = True
                time.sleep(0.05)
                self.K1.value = False
                self.J1.value = False
                self.L1.value = False
                # turns all off 



    