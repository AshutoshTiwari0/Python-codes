"""
print(10+5)
print(5*8)
print(7/7)
print(10/.5)
print(10%3)
print(10//7) #output will be 1 and not 1.somethibg bcoz // gives only the before point value
print(5**5) # ** is power ^ symbol

a=7
a=a*7
b=7
b*=7
print(a)
print(b)
"""

# comparison operators
print(10>5)
print(4 ==1)

print(10>=10)
print(1>0 and 7<10)

#we can have more than one and
print(10>4 and 4>2 and 1>0)
print(10>5 or 10>11) # true bcoz one is correct


a=4.0
print(id(a))

b=1.0*4.0
print(id(b)) # gives address
print(a is b)
print(a==b)


num=[1,2,3,4]
print(4 in num) # checks if 4 is in num
print(4 not in num) # checks if 4 is not in nums