#using dataclass 

from dataclasses import dataclass
@dataclass 
class carwithdataclass:
    color:str
    name:str

if __name__=="__main__":
    obj1=carwithdataclass("red","ferrari")
    obj2=carwithdataclass("black","mustang")
    obj3=carwithdataclass("black","mustang")
    print(obj1==obj2)
    print(obj2==obj3)


"""    
without data class 
class withoutdataclass:
    def __init__(self,color,name):
    self.name=name
    self.color=color

    def __eq__(self,other):
    return self.__dict__=other.__dict__

    if(__name__=="__main__"):
    obj1=withoutdataclass("black","porsche")
    obj2=withoutdataclass("black","porsche")
    obj3=withoutdataclass("red","ferrari")
    print(obj1==obj2)
    print(obj2==obj3)

#the above two codes are exactly same -> in dataclass we dont have to use any initialiser we can directly assign the variables
"""