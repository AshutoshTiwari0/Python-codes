class A:

        
    def printing(self):
        print("I am first class method")

class B(A):


    def printing(self):
        print("I will overtake/overrride")

if __name__=="__main__":
    obj=A()
    obj.printing()

    obj=B()
    obj.printing()