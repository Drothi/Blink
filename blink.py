import time
#MAIN#############################################################
#Pulse Lifebit####################################################
class blink():
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
                self.LAST_BLINK_TIME = now
                return self.lifebit
        if self.lifebit:
            # Is it time to turn off?
            if now >= self.LAST_BLINK_TIME + self.delay:       
                self.lifebit = False
                print(self.lifebit)
                self.LAST_BLINK_TIME = now
                return self.lifebit
#####################################################################
# CALL
#####################################################################
# import blink
#  
# b = blink(0.5)
# while True:
#     b.blink()  
              


