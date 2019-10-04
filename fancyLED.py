import time  #pylint:disable-msg=import-error
import board  #pylint:disable-msg=import-error
import random #pylint:disable-msg=import-error
import digitalio #pylint:disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint:disable-msg=import-error
class FancyLED:
    def __init__(self, p1, p2, p3):
        print("you just made an object!")
        self.K1 = p1
        self.J1 = p2
        self.L1 = p3
        self.K1 = DigitalInOut(p1)
        self.K1.direction = Direction.OUTPUT
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
        time.sleep(1)
        self.K1.value = False
        self.J1.value = True
        self.L1.value = False
        time.sleep(1)
        self.J1.value = False
        self.K1.value = False

    def blink (self):
        #do blink stuff
        print("blink")
        self.K1.value = True
        self.J1.value = True
        self.L1.value = True
        time.sleep(0.5)
        self.K1.value = False
        self.J1.value = False
        self.L1.value = False
        time.sleep(1)
    
    def chase (self):
        #do blink stuff
        print("chase")
        self.K1.value = True
        self.J1.value = False
        self.L1.value = False
        time.sleep(0.05)
        self.K1.value = False
        self.J1.value = True
        self.L1.value = False
        time.sleep(0.05)
        self.K1.value = False
        self.J1.value = False
        self.L1.value = True
        time.sleep(1)
        self.L1.value = False

    def sparkle (self):
            for whatever in range (0,50):
                n = random.randint (0,3)
                print(n)
                if n == 0:
                    self.K1.value = False
                    self.J1.value = True
                    self.L1.value = True
                if n == 1:
                    self.K1.value = True
                    self.J1.value = False
                    self.L1.value = True
                if n == 2:
                    self.K1.value = True
                    self.J1.value = True
                    self.L1.value = True
                if n == 3:
                    self.K1.value = False
                    self.J1.value = False
                    self.L1.vaule = True
                time.sleep(0.05)
                self.K1.value = False
                self.J1.value = False
                self.L1.value = False



    