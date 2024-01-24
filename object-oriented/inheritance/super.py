class Lamp:
    def __init__(self,name):
        self.name=name

    def turn_on(self):
        print(f"{self.name} is turned on")

    def turn_off(self):
        print(f"{self.name} is turned off")


class House(Lamp):
    def __init__(self,name):
        super().__init__(name)
        #we are accessing name parent class variable in sub class so we used super

    def turn_on(self):
        print(f"Now we overrriden lamp on feature. It will only open on whistle")

        #if we want parent class access
        #this turn on is of parent class->Lamp
        super().turn_on()
"""
ghar=House("Bungalow")
ghar.turn_on()
"""
ghar=House("Bungalow")
ghar.turn_on()
