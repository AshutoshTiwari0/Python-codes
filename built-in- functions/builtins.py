#introduction
#1)print
"""
maximum:int=max(8,5)
print(maximum)

maxim:list[int]=[1,2,3,4,5,6,7,8,9,10]
print(max(maxim))


#print()
print("console","output",1,2,3)
#separator built in
print("ash",10,"hello",sep="+")
#end built in
print("My name is Ashutosh", end=".")
"""

#2)enumerate()
"""
names:list[str]=["Ashutosh","Tiwari","Krishna"]

#printing using for
for i in names:
    print(str(names.index(i)+1)+" "+i)

#printing using enumerate
for i,name in enumerate(names):
    print(i," ",name)

"""
#3) round()
"""
nums=2.56154
print(round(nums))
print(round(nums,3))

"""
"""
#4) range()
r=range(1,11)
print(r.index(5))
print(list(r))

r1=range(1,10,2)
print(list(r1))

"""
# 5) globals-> returns all the global attributes
"""
var="global"

def hello():
    var2="local"
    return var2

print(globals())
"""

"""
#6) locals-> returns all the local attributes
def func():
    var="a"
    var2="b"

print(locals())

"""
"""
#7) all() and any() -> iterate over a list and return boolean values
list1:list[int]=[1,2,3,4,5,6,7,8,9,10]
list2:list[int]=[1,2,3,4,5,6,7,8,9,10]
value=all([list1,list2])
print(value)

list3:list[int]=[8,9,10]
list4:list[int]=[10]
value2=any([list1,list2])
print(value2)
"""

#8) isinstance()-> it checks whether an object belongs to a certain class or not 
"""
class vehicle:
    def __init__(self,name):
        self.name=name

class another:
    pass

if __name__=="__main__":
    obj=vehicle("Apache")
    obj2=vehicle("Hayabusa")
    newobject=another()

#checks whether obj belongs to vehicle or not
print(isinstance(obj,vehicle))
print(isinstance(newobject,vehicle)) #returns false bcoz it is of type another()

# isinstance can also check datatypes
var:int =5
dou:str="dj"
print(isinstance(var,int))
"""

"""
#callable()
class a:
    def do_something():
        print("doing..")
if __name__=="__main__":
    obj=a()
    print(callable(a))
    print(callable(obj.do_something))
"""

#filter(logic of filter, iterable to be filtered)
"""
list_of=["Ashutosh",19,"Tiwari",25]
def is_num(element):
    return isinstance(element,int)

filtered=list(filter(is_num,list_of))
print(filtered)
"""


#note: map and filter do not return lists. so we explicitly have to convert them.
#map()
"""
list_=[1,2,3,4,5,6,7,8,9,10]

def convert_to_str(i):
    return str(i)

new_list=map(convert_to_str,list_)
print(list(new_list))

"""
"""
#map->example 2
#inc every value by 10
list_nums= [1,2,3,4,5]

def inc_by_ten(i):
    return i+10

list_nums_inc_by_ten=map(inc_by_ten,list_nums)
#explicitly convert to list
list_nums_inc_by_ten_to_list:list[int]=list(list_nums_inc_by_ten)
print(list_nums_inc_by_ten_to_list)
"""

"""
#sorted()->it returns a new list
unsorted:list[int]=[7,5,1,2,9,8,4,3,2,0]
sorted_list:list[int]=sorted(unsorted)
print(sorted_list)

#using sort()-> this sorts and replaces the original list so it does not return a new list
unsort:list[int]=[5,4,65,8,5,1,2,0]
unsort.sort()
print(unsort)

#sorting in reverse

new_list:list[int]=[4,5,2,1,7,8,9,6,3]
new_list.sort(reverse=True)
print(new_list)

#sorting of alaphabets
list_of_letters:list[str]=['A','L','G','B','a']
list_letters_sorted:list[str]=sorted(list_of_letters)

print(list_letters_sorted)
"""

"""
#eval()->stands for evaluate
user_input=input("Enter your equation")

print(eval(user_input))

#a unique concept

magic_str:str="""
#10* "hello"
"""

print(eval(magic_str))#->prints 10 hello's

"""
"""
#exec()-> stands for execute
user_input=input("enter code")
exec(user_input)
"""

#zip()->takes tuples and put them together
tup1:tuple=(1,2,3)
tup2=("Ashutosh","controller","kid")
zipped_together=zip(tup1,tup2)
print(list(zipped_together))

