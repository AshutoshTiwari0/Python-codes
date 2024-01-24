# to create a custom exception we just have to inherit exception class 
class myownerror(Exception):
    
    def __init__(self, num,error):
        self.num=num
        self.error=error
        super().__init__(f"{self.num} is less than 0. Error encountered-> {self.error}",self.num,self.error)

    def __str__(self):
        return f"{self.num} is less than 0. Error encountered-> {self.error}"



try:
    raise myownerror(-7,"negative value exception")
except myownerror as E:
    print(E)
    print(E.args)