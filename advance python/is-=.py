# is -> checks wrt to memory address
# == -> it checks wrt to value


"""
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def __eq__(self, other):
        return self.__dict__==other.__dict__
    
if __name__=="__main__":
    obj=Animal("Elephant","Mammal")
    obj2=Animal("Elephant","Mammal")
    if obj is obj2:
        print("Memory address equal->is")
    else:
        print("Memory address not equal->is")

    if obj==obj2:
        print("value is equal->==")
    else:
        print("value is not equal->==")


"""
# 2nd example->
a=500
a=a+500
b=1000
print("id of a is="+str(id(a))+" "+"id of b="+str(id(b)))
print(a is b)
#expected output-> false for is. true for ==
print(a==b)