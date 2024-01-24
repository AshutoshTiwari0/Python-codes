class Fruit:
    global a
    a=10
    def __init__(self):
        
        print(a)
    
obj=Fruit()

#this code shows that an initialiser is a constructor.
#here as soon as we just created the object at line 8 our self constructor worked and printed the value of a