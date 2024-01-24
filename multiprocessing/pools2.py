"""
import multiprocessing as mp
from timewaste import get_time
import time





def add_numbers(*args)-> float:
    time.sleep(2)
    return sum(args)



@get_time
def main():
    print(f"number of cores are {mp.cpu_count()}")

    value=((1,2),(3,4),(5,6),(7,8))

    with mp.Pool() as pool:
        results=pool.starmap(add_numbers, value)
        print(results)



if __name__=="__main__":
    main()


"""
#Mulitple pools
import multiprocessing as mp
from timewaste import get_time
import time
import functools

def func_A(param):
    time.sleep(2)
    return param


def func_B(param):
    time.sleep(2)
    return param


def func_C(param,param2):
    time.sleep(2)
    return param, param2


def map_func(func):
    return func()

@get_time
def main():
    print(f"the number of cores avaialble are {mp.cpu_count()}")


    a=functools.partial(func_A,'A')
    b=functools.partial(func_B,'B')
    c=functools.partial(func_C,'C1','C2')

    with mp.Pool() as pool:
        results=pool.map(map_func, [a,b,c])
        print(results)
if __name__=="__main__":
    main()