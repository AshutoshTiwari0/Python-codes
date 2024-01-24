"""
class Vehicle:
    def __init__(self, power,brand): 
        self.power=power
        self.brand=brand


if __name__=="__main__":
   bmw= Vehicle(500,"BMW")
   bmwfake=Vehicle("BMWFAKE","1000")

   print(bmw==bmwfake)
"""
#__eq__ is used to compare two classes

class Vehicle:
    def __init__(self, power,brand): 
        self.power=power
        self.brand=brand

    def __eq__(self, other):
        return self.__dict__==other.__dict__

if __name__=="__main__":
   bmw= Vehicle(500,"BMW")
  # bmwfake=Vehicle("BMWFAKE","1000")
   bmwfake=Vehicle(500,"BMW")

   print(bmw==bmwfake)