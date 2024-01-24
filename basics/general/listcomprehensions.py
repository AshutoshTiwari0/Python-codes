#normal way of creating a list

list_of_nums=[]

for i in range (10):
    list_of_nums.append(i)

print(list_of_nums)



#using comprehensions
list_using_comprehensions=[j for j in range(10)]
print(list_using_comprehensions)

#inputing only even numbers in list without comprehension
even_list=[]
for i in range (10):
    if i%2==0:
        even_list.append(i)
    

print(even_list)
    

#inputing only even numbers in list with comprehension
even_comprehension_list=[k for k in range (10) if k%2==0 ]
print(even_comprehension_list)


even_comprehension_list2=[k*2 for k in range (10) if k%2==0 ]
print(even_comprehension_list2)


car_comprehension=["Buggati","Pagani","Aston Martin"]

upper_case= [cars.upper() for cars in car_comprehension]
print(upper_case)