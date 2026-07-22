class LightBulb:
    def __init__(self):
        self.is_on=False
        self.burn_count=0

    def turn_on(self):
        if self.is_on==False:
            self.is_on=True
            self.burn_count+=1
        else:
            print("Bulb is on , no change")

    def turn_off(self):
        if self.is_on==True:
            self.is_on=False
    
    def get_status(self):
        print("current status of bulb", self.is_on)
        print("total burn status",self.burn_count)

bulb = LightBulb()
bulb.turn_on()
bulb.turn_on()   # Already on, shouldn't increase burn_count again
bulb.turn_off()
bulb.turn_on()
bulb.get_status() # Should print: Status: OFF (or ON depending on final state) and Burn Count: 2