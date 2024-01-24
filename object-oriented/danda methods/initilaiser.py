#initilaiser-> to initialise.
class initilaiser:
    def __init__(self,model,color):
        self.model=model
        self.color=color
        print(f"the car name is {self.model} of color {self.color}")

    def driving(self):
        print(f"{self.model} with color {self.color} is driving")

if __name__=="__main__":
    initilaiser = initilaiser("Aston martin","Silver")