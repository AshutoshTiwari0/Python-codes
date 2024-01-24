"""
from functools import wraps
from time import perf_counter
import sys

def fibo(n)-> int:
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

#lets calculate time it took

start_time=perf_counter()
sum:int=fibo(20)
end=perf_counter()

timetook=end-start_time

print("time it took"+str(timetook))
print(sum)

"""
"""
#fibonacci using memoization to improve performance
from functools import wraps
from time import perf_counter
import sys

def memoize(func):
    cache:dict={}

    @wraps(func)
    def wrapper(*args,**kwargs):
        key=str(args)+str(kwargs)

        if key not in cache:
            cache[key]=func(*args,**kwargs)

        return cache[key]
    return wrapper


def fibo(n)-> int:
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)



start_time=perf_counter()
sum:int=fibo(5)
end=perf_counter()

timetook=end-start_time

print("time it took"+str(timetook))

"""


#memoization is inbulit in python we dont have to do this much
import functools
from time import perf_counter
import sys

@functools.cache
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
s=fibo(100)
print(s)