class animal:
    def __init__(self, species, color):
        self.species=species
        self.color=color
        print("this is a constructor")
        print(f"{species} is of color-{color}")
        

    def trick(self):
        print("doing tricks")

tiger=animal("mammal","White")
tiger.trick()


