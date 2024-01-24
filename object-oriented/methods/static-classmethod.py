class calc:

    #global variable will be accessed by class method
    var:int
    def __init__(self,name):
        self.name=name
    
    #a normal method
    def description(self):
        print(f"{self.name} is a calculator")


    @staticmethod
   # static method is a general purpose method which does not require self attribute it can function without self inside or outside the class
    def addition(a,b):
        print(a+b)

    @classmethod
    #this access the global varibales
    def class_ka_method(cls,name):
        return cls(name)





#obj=calc("FX82")
obj=calc.class_ka_method("FX82")
obj.description()
# referring to static method using object
obj.addition(100,1)
# referring to static method using class
calc.addition(500,250)

