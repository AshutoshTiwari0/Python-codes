text="Text  'Ash'  "
print(text)

# this is not allowed bcoz compiler gets confused that where is tiwari's starting "
#text2="Ashutosh "Tiwari" 

text3='Ashutosh "Tiwari" coding'
print(text3)

# /n is used for printing in new line
text4= "Ashutosh \n Tiwari"
print(text4)

# multi line strings

str7="""We will win 
        the next 
        world cup"""
print(str7)

# currently we have no space b/w each string we have to manually add it. python says why to add manually. we will give you f strings. you will chill.
# F(Formatted)- strings
print("Thala"+"7"+"for a reason")

# f string
strin=f"Hello"
print(strin)

var="Ashutosh"
var2="YT"
ftxt=f"1 {var}{var2} 5"
print(ftxt)


# use of f string demo

#without f string
# output is-> the product of4and7is28
x=4
y=7
print ("the product of" + str(x) +"and"+ str(y) + "is"+ str(x*y))


#with f string
# output is->the product of 4 and 7 is 28
x1=4
y1=7
p=x*y
print (f"the product of {x1} and {y1} is {x1*y1}") 