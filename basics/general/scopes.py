#global scope-> a variable defined outside a method can be used anaywhere globally
#local scope-> a variable defined inside a function can only be used inside and no where else outside the function 




a=10

def printlocal():
    b=4 # a local scoped variable
    print(a)
    print(b)

    def printb():
        print(b)
    printb()
print(a)


#print(b) we can not do so bcoz b is only accessible inside the function
printlocal()


#<---nonlocal and global-->


x=10

def func():
    x=20
    print("inner",x)

print("outer", x)
func()


# waht if we want to have local value evrywhere. 
#just use global keyword

#this x is global
x=10

def func():
   global x
   x=20
   print("inner",x)

func()
print("outer", x)



#non local keyword
print("non local")

def func():
    x = 20

    def innerfunct():
        nonlocal x
        x = 10
        print("inner", x)

    innerfunct()
    print("outer", x)

func()
