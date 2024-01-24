class animal:
    def __init__(self, color,family):
        self.color=color
        self.family=family
        print("initilaisation done")

        #__str__ means string


    def __str__(self):
        return f"the animal is of color {self.color} and the family is {self.family}"
    
    #__repr__ means representation
    def __repr__(self):
        return f"the animal is {self.color} and belongs to {self.family}"


#making object of class to initialise the init
if __name__=="__main__":
    bm= animal("black mamba","reptile")
    print(bm)
    print(bm.__repr__())