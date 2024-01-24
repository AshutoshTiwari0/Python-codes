#arguments and keyword arguments
#print(1,2,3,4,5,6,7)
#here print() method is taking multiple arguments 1,2,3...

#what if we have multiple arguments and want only one variable to accept them
# we use *variable_name
"""
def greet(*people: str):
   print(people)
   for name in people:
      print(f"Hello,{name}")
greet("ashutosh","tiwari","pramod")
"""
#since we have multpile names now if we want to pass a single variable we can not do so
# to pass single variable we must define it first before the *parameters
"""
def greetagain(age,*people):
   print(str (age)+" "+str(people))
   for names in people:
      print(f"Hi, {names}") 

greetagain(45,"Ashutosh","Krishna","Abhishek","Mathur")
"""
# keyword arguments
#name="ash",age=10,place"=india" ye hai ek keyword arguments
def kwordargu(**kwargs):
    print(kwargs)

kwordargu(name="ash",age=10,place="india")
   




