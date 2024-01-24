class fruits:
    def __init__(self,name,color):
        self._name=name
        self._color=color

#  _ is a convention for private variables in python
    @property
    def namecolor(self):
        print(f"{self._name} is used along with {self._color}")
        return self._color, self._name
    
    @namecolor.setter
    def namecolor(self,value:str):
        print(f"{self._name} is now {value}")
        self._name=value

if __name__=="__main__": 
    fruitt=fruits("Apple","Red")
    fruitt.name="pine"
    print(fruitt.name)

#print(fruits._color)
    fruitt.namecolor          