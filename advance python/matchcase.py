#it is switch case only


#without match case

a:int=5
"""
if a%2==0:
    print("even")
elif a%2==1:
    print("odd")
else:
    print("neither odd nor even")
"""

#using match case


match a % 2:
    case 0:
        print("even")
    case 1:
        print("odd")
    case _:
        print("neither odd nor even")

           


