import pulseio
import time
class RGB: # this is a class. this is the what x "equals", and will later be "plugged" into the classes.objects.and.modules file when called
    kind="colors"
    def __init__(self, r, g, b):
        print("you just made an object!")
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)
# establishes pins for red, green, and blue, 
    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r

# below until rainbow; using red, green. and blue, combine those colors to make other colors
    def red(self):
        # do red stuff
        self.pwm_r.duty_cycle = 0 # turns red on
        self.pwm_g.duty_cycle = 2**16-1 # turns green off
        self.pwm_b.duty_cycle = 2**16-1 # turns blue off 

    def blue(self):
        # do blue stuff
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def magenta(self):
        #do magenta stuff
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle= 0

    def green(self):
        #do green stuff
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle= 2**16-1

    def cyan(self):
        #do cyan stuff
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle= 0

    def yellow(self):
        #do yellow stuff
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle= 2**16-1

    def rainbow(self): # slowly fades through all of the colors, beginnning with red, ending with purple 
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
        for val in range (0,2**16-1, 64): # sets the range, turns all off, begins increasing in incremtns of 64
            self.pwm_r.duty_cycle = val
            self.pwm_g.duty_cycle = 2**16-1 -val
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(.01)
        for val in range (0,2**16-1, 64):
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = val
            self.pwm_b.duty_cycle = 2**16-1-val
            time.sleep(.01)
        for val in range (0,2**16-1, 64):
            self.pwm_r.duty_cycle = 2**16-1-val
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = val
            time.sleep(.01)