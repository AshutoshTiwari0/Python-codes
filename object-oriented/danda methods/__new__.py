"""
class connection:
    __instance=None

    def __new__(cls,*args,**kwargs):
        if cls.__instance=="":
            print("Trying to Connect")
            cls.__instance=super().__new__(cls)
            return cls.__instance
        else:
            print("Already Connected")
            return cls.__instance
        
    def __init__(self):
        print("connected")

obj1=connection()
obj2=connection()
"""


#Example 2->
class Vehicle:
    def __new__(cls,wheels):
        if wheels==2:
            return twowheeler()
        elif wheels==4:
            return fourwheeler()
        else:
            return super.__new__(cls)
        
    #this will happen if wheels are not 2/4
    def __init__(self,wheels:int):
        self.wheels=wheels
        print(f"Vehicle has {wheels} no of wheels")

class twowheeler:
    def __init__(self):
        print("on a motorbike")

class fourwheeler:
    def __init__(self):
        print("on a four wheeler ")
        

tw=Vehicle(2)
fw=Vehicle(4)

