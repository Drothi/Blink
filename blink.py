import time
#MAIN#############################################################
#Pulse Lifebit####################################################
class blink():
    lifebit = False 
    BLINK_ON_DURATION = 0.5
    BLINK_OFF_DURATION = 0.5
    LAST_BLINK_TIME = -1
    def blink(delay):
        now = time.monotonic()
        if not blink.lifebit:
            # Is it time to turn on?
            if now >= blink.LAST_BLINK_TIME + delay:
                blink.lifebit = True
                print(blink.lifebit)
                blink.LAST_BLINK_TIME = now
        if blink.lifebit:
            # Is it time to turn off?
            if now >= blink.LAST_BLINK_TIME + delay:       
                blink.lifebit = False
                print(blink.lifebit)
                blink.LAST_BLINK_TIME = now

class blink2:
    def __init__(self,delay):
        self.delay = delay
        self.lifebit = False 
        self.BLINK_ON_DURATION = 0.5
        self.BLINK_OFF_DURATION = 0.5
        self.LAST_BLINK_TIME = -1
    def blink(self):
        now = time.monotonic()
        if not self.lifebit:
            # Is it time to turn on?
            if now >= self.LAST_BLINK_TIME + self.delay:
                self.lifebit = True
                print(self.lifebit)
                LAST_BLINK_TIME = now
        if self.lifebit:
            # Is it time to turn off?
            if now >= self.LAST_BLINK_TIME + self.delay:       
                self.lifebit = False
                print(self.lifebit)
                self.LAST_BLINK_TIME = now

class blink3():

    def __init__(self):
        self.lifebit = False
        self.BLINK_ON_DURATION = 0.5
        self.BLINK_OFF_DURATION = 0.5
        self.LAST_BLINK_TIME = -1

    def blinkOnOff(self):

        now = time.monotonic()
        if not self.lifebit:
            # Is it time to turn on?
            if now >= self.LAST_BLINK_TIME + 0.5:
                self.lifebit = True
                print(self.lifebit)
                self.LAST_BLINK_TIME = now
        if self.lifebit:
            # Is it time to turn off?
            if now >= self.LAST_BLINK_TIME + 0.5:
                self.lifebit = False
                print(self.lifebit)
                self.LAST_BLINK_TIME = now                


