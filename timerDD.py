import time
#MAIN#############################################################
#Pulse Lifebit####################################################
class blink():
    def __init__(self,delay):
        self.delay = delay
        self.pulse = False 
        self.BLINK_ON_DURATION = 0.5
        self.BLINK_OFF_DURATION = 0.5
        self.LAST_BLINK_TIME = -1
    def blink(self):
        now = time.monotonic()
        if not self.pulse:
            # Is it time to turn on?
            if now >= self.LAST_BLINK_TIME + self.delay:
                self.pulse = True
                print(self.pulse)
                self.LAST_BLINK_TIME = now
        if self.pulse:
            # Is it time to turn off?
            if now >= self.LAST_BLINK_TIME + self.delay:       
                self.pulse = False
                print(self.pulse)
                self.LAST_BLINK_TIME = now
        return self.pulse
#####################################################################
# CALL
#####################################################################
# import blink
#  
# b = blink(0.5)
# while True:
#     b.blink()             


