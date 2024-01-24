"""

text="Ashutosh"
print(text)

number=7
print(number)

decimal=.25
print(decimal)

#list
number=["Ashutosh","Aditya"]

#tuple
nums=(1,2,3,4,5,)


#dictionary-> like a hashmap in java
num={"User" : "Ashutosh" ,
     "Id" : "A7605"}
print(num)

#set-> a set has no duplicate
unique={1,1,2,4,8,55,55,55}
print(unique)  #output will be -> 1,2,4,8,55. but will be randomly arranged.

# frozenset-> can not be changed later
unique_num=frozenset({1,2,3,4,5,6})
print(unique_num)

#boolean
identity= True

is_empty= None

print(is_empty)

#type hinting-> just for readabilty does not affect program 
number: int = 5.2
print(number)

name: str=5
n: str="ash"
print(name)
print(n)

#type coversion

name="ashutosh"# this is a string
num=7# this is an integer 
#print(name+" "+num)# error-> we can not add string and integer
print(name+str(num))

print(type(name))

num1='100'
num2=10

result=num1+str(num2)
print(result)

print(int(num1)+num2)

#integers
a=10
b=1000
c=-10
print(a+c)

#more on data types

#booleans-> true or false

print(False==0) #output is true
print(True+True)  # output is 1+1=2

<-----------LISTS---------->

#lists
rappers:list=['KR$NA','Spectra','Talha Yunus']
print(rappers)

# list can also have diff data types
data=["XYZ",784]
print(data)

football=["Hello","I","am","Jose","Mourhino"]
print(len(football))
print(football[0])
print(football[1])
print(football[2])
print(football[3])
print(football[4])
print("\n")
# if we use -ve index we will get elements in reverse
food : list[str]=["Bread","Apple","Pancakes"]
print(food[0])
print(food[-1])
print(food[-2]) 
print(food[-3])

#taking multiple elemnts from a list
numb=[1,2,3,4,5,6,7,8,9,10]
print(numb[1:5]) # it is like substring(i,j) from ith index (i-j) number of elements will be picked.
print(10 in numb)

#accessing elemnts in a list
contacts=["ash","harry","navin","reddy","luigi"]
print(contacts[3])
contacts[3]="Raghav"
print(contacts[3])
print(contacts)

names=["Ash","Tiw","Ri","Prabh"]
names[0:3]={"Utopia","Travis","Token"}
print(names)

names[1:2]={"Try","out"}
print(names)
u=[1,2,3,4]
u.insert(2,"Ash")
u.append("last")
print(u)

games=["cod","valorant","bo2"]
games.append("warzone")
print(games)

mobile_games=["Hill climb","CODM","Alto's Odyssey"]
games.extend(mobile_games)
print(games)
"""

"""
"creatign an array/list"
fruits=["apple","orange","kela","pineapple"]
fruits.remove("orange")
print(fruits)

# we can also use .pop(). we have to tell index if we do not tell it index it will by default remove the last one.
fruits.pop()
print(fruits)

animals=["lion","tiger","elephant","horse"]
animals.pop()# since there is no index defined it will automatically remove the last element
print(animals)

brands=["dell","apple","hp","lenevo"]
brands.sort()# sorts alphabetically
print(brands)


#<--------TUPLE----------->
         
#tuple
# we can change a list but not a tuple
# duplicates are allowed
# tuple is made by , not by ()

devices: tuple=("Laptop","Phone","Phone","Tab","Console")
# we cannot change anything inside a tuple later
#devices[0]="Asus" # error
print(devices)

# we can convert list to tuple and vice versa
# making  a list
languages:list=["Java","c","Python","Javascript"]
# coverting list to tuple
tuple_of_languages:tuple=tuple(languages)
print(tuple_of_languages)
# converting tuple to list
languages_tuple=("Java","c","Python","Javascript")


# coverting list to tuple
list_of_languages:list=list(languages)
print(list_of_languages)

# accessing elements of a tuple
tuple_of_cars:tuple=("Aston martin","Buggati","Pagani")
print(tuple_of_cars[0]) # aston martin
print(tuple_of_cars[1]) # buggati
print(tuple_of_cars[2]) # pagani
print(tuple_of_cars[-3]) # go from backwards so ->Aston martin
#print(tuple_of_cars[3]) #out of range error
print(tuple_of_cars.__len__())

#count() tells no of times element occurs
print(tuple_of_cars.count("Aston martin"))# 1

#if we two same elemnts it will give first index of occurence
tuple_of_bikes=("Ducati","Kawasaki","Honda","Yamaha","Honda")
print(tuple_of_bikes.index("Honda"))


a,b,c,d,e=tuple_of_bikes
print(a)
print(b)
print(c)
print(d)
print(e)


# a stores first. * means rest will go to b
a,*b=tuple_of_bikes
print(a)
print(*b)

#<-----------SETS----------->
#sets ->have unique values, unchangeable
set_of_num : set= {1,2,3,14,5,16,87,8,9}

print(set_of_num)
print(len(set_of_num))

fruits_set={"orange","pineapple","mango"}
fruits_set.add("guava")
print(fruits_set)
# we can add multiple data using update()
fruits_set.update(["Ash","Krish","Messi"])
print(fruits_set)

fruits_set.remove("mango")
print(fruits_set)

#merging 2 sets
set1 :set={"chess","Table tennis","Carrom"}
set2 : set={"football","cricket","Rugby"}
print(set1.union(set2))
#merging by or operator |
print(set1 | set2)

#intersection_update()-> returns the common elements b/w the 2 sets
n={1,2,3,4,5,6,7,8,9,10}
e={2,4,6,8,10}
n.intersection_update(e)
print(n)


set3={1,2,5,8,9}
set4={1,2,5,8,7}
set3.symmetric_difference_update(set4)
print(set3)

"""

"""
#empty set
empty_set=set()
print(type(empty_set))
"""


#dictionaries
name={"id": 7605222,
      "name": "Ash"}
print(name)
print(len(name))
# accessing a dict
naam=name["name"]
print(naam)
id_code=name["id"]
print(id_code)

print(name.get("id"))

print(name.keys())

print(name.values())

# changing values inside of a dict
name['id']=76666
print(name)

print(name.items()) # items() returns a dict data type so we can convert to lists
print(list(name.items()))

#update()

veggies={"potato":75,
         "tomato":100,
         "spinach":80}
veggies.update({"onion":99})
print(veggies)
veggies.pop("spinach")
print(veggies)

 # no index is defnied so removes the last one by default
veggies.popitem() 
print(veggies)

# nested dictionaries

nested_dict={"user1":"Ash",
             "user2":"Tiw",
             "Items": {"Apple":"10",
            "bannana": "20" }
          } 
print(nested_dict)
print(nested_dict.setdefault("keynamewhichdoesnotexsist", "no such key exsist"))
