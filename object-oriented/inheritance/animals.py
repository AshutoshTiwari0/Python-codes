#animal is base class/ parent class

class animals:
    def __init__(self, name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

#creating a sub class
# derived class(base class)
#below line is inheritance
class Racoon(animals):
    def __init__(self, name,species):
        #super->used for calling base class parameters
        #here name is defined in base class so we use super initiliaser name
        super().__init__(name)
        #here name is of class animals wala 
        self.species=species

#steal is unique charcateristic of racoon class
    def steal(self):
        print(f"{self.name} has a habit of stealing")



class Seagull(animals):
    def __init__(self, name,species):
        #super->used for calling base class parameters
        #here name is defined in base class so we use super initiliaser name
        super().__init__(name)
        #here name is of class animals wala 
        self.species=species

    #uniques to seagull
        #since seagull inherited animals it directly have the eat sleep methods
    def steal(self):
        print(f"{self.name} has a habit of stealing babies")

    def fly(self):
        print(f"{self.species} can fly and the name is {self.name}")


if __name__=="__main__":
    obj=Racoon("Doreamon","Sans Serif")
    obj.sleep()
    obj.steal()
    obj.eat()
    

    seagull=Seagull("Seagull","Bird")
    seagull.eat()
    seagull.steal()
    seagull.sleep()
    seagull.fly()    
