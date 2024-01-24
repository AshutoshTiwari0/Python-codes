#aim-> to create a class booster which will be responsible for boosting the speed of ferrari
class car:
    def __init__(self,mileage,speed):
        self.mileage=mileage
        self.speed=speed

    def topspeed(self):
        print(f"the top speed of the vehicle is {self.speed}")

class booster(car):
    def __init__(self,mileage,booster,speed=None):
        #self.speed=speed
        super().__init__(mileage,speed)
        self.booster=booster
        #self.mileage=mileage
        print("speed without booster is"+str(self.speed))
        
    def speedinc(self):
        self.speed=self.booster+self.speed
        print("the new speed is "+str(self.speed))


#making object
if __name__=="__main__":
    ferrari=car(7,300)
    ferrari.topspeed()
    print( "the mileage of ferrari is "+ str(ferrari.mileage))
    boost_in_speed=booster(10,25,300)
    boost_in_speed.speedinc()

    



