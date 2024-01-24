class Animal:
   #currently this is shared once only na ki after each object creation tricks: list[str]=[]
    tricks: list[str]=[]

    def __init__(self,name) :
        self.name=name
        





    def do_tricks(self,trick_name):
        self.tricks.append(trick_name)
        
    
if __name__=="__main__":
    a=Animal("Dog")
    a.do_tricks("Jumping through a Hoop")
    a.do_tricks("Dog sit on whistle")
    print(f"tricks of dog are {a.tricks}")

    
    dolphin=Animal("Dolphin")
    dolphin.do_tricks("Playing with ball on nose")
    print(f"tricks of dolphin are {dolphin.tricks}")
    

#class variables will be avaialbale to all objects
#instance variables are only avaiable for the particular object at a time
#refer to them using self

