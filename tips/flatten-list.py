from typing import Iterable

people:list[str]=[
    ["Ash","Tiwa"], 
    ["Adnan","Rajjo"]
                ]
# now we have a 2d list
new_list=[]
for names in people:
    for name in names:
        new_list.append(name)


#2nd way using list comprehensions
new_list2:list[str]=[name
                    for names in people 
                    for name in names 
                    ]
print(new_list)
print(new_list2)


#3rd way -> importing iterable from typing

def flatten(iterable):
    list_=[]
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item,str):
            list_.extend(flatten(item))
        else:
            list_.append(item)

    return list_

if __name__=="__main__":
    sample=["ash","tiw",[1,2,3,4,["toad","tie"],5]]
    print(flatten(sample))