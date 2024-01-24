
class Lamp:
    def __init__(self, model:str,color:str):
        self.model=model
        self.color=color

    def turn_on(self):
        print(self.model, "is ON")
    
    def turn_off(self):
        print(self.model, "is OFF")

    def describe(self):
        print(f"The model of lamp is {self.model} and color is {self.color}")
    
#creating instance/object of class
red_lamp=Lamp("IR Table Lamp","Red")
red_lamp.turn_on()
red_lamp.turn_off()
red_lamp.describe()

#first object is created so abhi self is pointing to this object only


#creating another object
blue_lamp=Lamp("UV A","blue")
print(blue_lamp.model)
print(blue_lamp.color)
blue_lamp.describe()
blue_lamp.turn_off()
blue_lamp.turn_on()
#now self will be pointing to this object


#self-> it points to the current object which is being executed
# like first it will refer to red lamp object so every self points to the current object which is red_lamp
# then after this object execution it refers to second object blue lamp
#so whole program executes for blue one.














