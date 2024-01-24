#quantities which do not vary are declared using enum.
#like a bulb it is going to be either true(ON) or false(OFF)


from enum import Enum as e


"""
class State(e):
    on=1
    off=0

light=State.on
dark=State.off

if light==State.on:
    print("the light is on")
elif light==State.off:
    print("The lamp is off")

"""

class cars(e):
    buggati="Veyron"
    pagani="Huayra"
    lamborghini="Sian"

model=cars.buggati
   

if model==cars.buggati:
    print("the car is "+str(model.value))
elif model==cars.lamborghini:
    print("the car is "+str(model.value))
elif model== cars.pagani:
    print("the car is"+str(model.value))
else:
    print("the car is from a different brand")

