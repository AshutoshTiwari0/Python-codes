"""
def greeting(name: str):
    print(f"Hello {name}")

greeting("Ashutosh")
greeting("Python")
"""
"""
def do_something():
    for i in range(5):
        print("doing something")
    
    print("function is completed")

do_something()
"""
#parameters and arguments
def greet(name:str, greeting:str="Namaste"):
    print(f"{greeting}" ,name)
greet("Ashutosh")
greet("Tiwari ji")
 

def human(name, age, height):
    print(f"name is {name} age is {age} height is {height}")

human("Ashutosh",10,175)


# now we want to set a default value ->age is suppose like 18
# since we defined age as 18 uske baad aane wale parameters mai compulsory hota hai value dena 
# here bcoz we gave age a value of 18 it makes it compulsory to give height a parameter
def characteristics(name:str, height:int,age:int=18):
    print(f"name is {name} age is {age} height is {height}")

characteristics("Ashutosh",180)