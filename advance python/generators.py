"""
def gen(n:int):
    for i in range(n):
        yield i
        #yield here tells that our function is generator


if __name__=="__main__":
   output= gen(10)
   print("1st",next(output))
   print("2nd",next(output))
   print("3rd",next(output))
   print("4th",next(output))
   print("5th",next(output))
   print("6th",next(output))
   print("7th",next(output))
   print("8th",next(output))
   print("9th",next(output))
   print("10th",next(output))
   print("11th error",next(output))

"""
"""
   #next gives one value at a time 
   suppose we want 10 values
   1<-next
   then next will give 2
   then 3
   ... then 10 and it will end 

   yeild keyword efines a generator
   """
"""
def generate_even(a):
    for i in range (a):
        if i%2==0:
            yield i

ans=generate_even(10)
for value in ans:
    print(value)

"""
#we can also make a genrator comprehension
nums=(i for i in range(10))
our_ans=list(nums)
print(our_ans)


nums2=(i for i in range(10))
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(next(nums2))


"""
summary -> generator is used to get one value at atime
if a function has a yield keyword that is a generator 
we can get next values using next()
"""