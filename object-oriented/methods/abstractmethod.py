# to implelemnt any abstarct method we have to import it
from abc import ABC,abstractmethod

class Phone(ABC):
    def __init__(self,model):
        self.model=model

    @property
    @abstractmethod
    def battery(self):
        pass

    #annotation is responsible for handling whtehr is it is definitely an abstarct method or not
    @abstractmethod
    def call(self,name:str):
        pass


#we have to define abstract methods by inheriting it is necessary
class Motorola (Phone):
    def __init__(self, model):
        super().__init__(model)

        #since we are implementing base class methods we have to define super
        #but python does that automatically we dont have to explicitly write it

    #we have to define our abstract methods after inheriting
    @property
    def battery(self):
        print("Low battery")
        

    def call(self, name: str):
        self.name=name
        print(f"Call from {name}")
        

obj=Motorola("one fusion plus")
obj.battery
obj.call("Uttar Pradesh")


