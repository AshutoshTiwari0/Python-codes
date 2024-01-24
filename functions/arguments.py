"from krish naik this topic"
"""def hello(name,age=19):
    print(f"Hello {name} you are {age} years old")

hello("Ashutosh",88)"""

def hello(*args,**kwargs):
    print(args)
    print(kwargs)

#hello("Ash","Tiwa",age=19,dob=2004)


tup_to_list=list(("Ash","tiw"))
dict_val={'age': 19, 'dob': 2004}

#hello(tup_to_list,dict_val)
hello(*tup_to_list,**dict_val)

