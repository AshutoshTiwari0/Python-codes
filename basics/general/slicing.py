list_nums:list=list(range(21))
print(list_nums)

#slicing is done using :: symbol
# this is our current list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list_nums[::3])
# it will print every third element of list

print(list_nums[10::3])


list_new=[4,5,8,7,9,15,45,48,12,58]
print(list_new[7::2])
# explanation-> 7 here signifies the index from where the array is to sliced and 2 defines after what gap the next element will be printed
# so here 7th index value is 48 and after 48 second element will be printed so 58
# output-> 48,58


list_num_value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list_num_value[5::3])
# expected output-> 5th index se har 3rd value->6,9,12,15,18

#similarly if we want this thing only in a specific range like x se y tak print numbers with gap of z
print(list_num_value[10:19:3])
# expected output->10 th index se har 3rd element till 19th index
#->11,14,17

#print all numbers after certain index
print(list_num_value[10:])

#print all numbers before certain index
print(list_num_value[:10])

#printing all
print(list_num_value[:10]+list_num_value[10:])

