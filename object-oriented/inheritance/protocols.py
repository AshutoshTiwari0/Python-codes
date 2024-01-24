from typing import Protocol
class Printable(Protocol):
    pages:int
    def __init__(self):
        super().__init__()

    def print(self):
        pass

    def recycle(self):
        pass


#class must have the protocol methods
class Book:
    pages:int
    def __init__(self,title):
        super().__init__()
        self.title=title

    def print(self):
        print("Printing book",self.title)

    def recycle(self):
        print("Recycling book",self.title)

def print_book(Printable):
    Printable.print()

#we created another class
class Magazine:
    pages:int
    def __init__(self,title):
        super().__init__()
        self.title=title

    def print(self):
        print("Printing Magazine",self.title)

    def recycle(self):
        print("Recycling Magazine",self.title)

def print_magazine(Printable):
    Printable.print()

obj=Book("Rich Dad Poor Dad")
obj.print()


Printable=Magazine("Donut Media Magazine")
Printable.print()