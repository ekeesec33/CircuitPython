import pulseio
import time
class RGB:
    kind="colors"
    def __init__(self, r, g, b):
        print("you just made an object!")
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)

    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r


    def red(self):
        # do red stuff
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1

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

    def rainbow(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
        for val in range (0,2**16-1, 64):
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