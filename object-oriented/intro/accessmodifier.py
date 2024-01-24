class Car:
    def __init__(self, color,brand,platform):
        self.__color=color
        self.brand=brand
        self._platform=platform
        #we only want to access brand and not color
        #convention->
        """
        _var=protected
        __var=private
        """
    def access(self):
        print(self.brand+" "+self.__color+" "+self._platform)

    def __working(self):
        print(f"{self.brand} is racing")

    
        
car=Car("Black","Rolls",11475485)
car.access()
#print(car.__color)# this can not be accessed bcoz it is a private variable
#working is now private
#car.working()

#protected ->Accessed using only inheritance