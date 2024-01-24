# a normal function
def square(n:int)-> int:
    return n*n


ans=square(5)
print(ans)


# a lamda function
# we always have to store a lamda function somewhere whether in a class or a variable always store it.

square_lamda=lambda n: n*n
print(square_lamda(5))

#filter a list using lamda
list_nums=[1,2,3,4,5,6,7,8,9,10]

filtered_list:list[int]= list(filter(lambda n:n%2==0,list_nums))
print(filtered_list)


