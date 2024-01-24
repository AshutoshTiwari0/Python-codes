"""
import time

start=time.perf_counter()


for i in range(10**4):
    pass

print("done")
end=time.perf_counter()
time_took=end-start
print("time it took",time_took)


"""

# another way to find time
import time
import timeit

def doing(first,second):
    for i in range(10**2):
        pass

    return first*second

def doing2():
    for i in range(10):
        p=i*i

    print(p)


def get_time(func:str,repeat:int,number:int):
    speed=min(timeit.repeat(func,repeat=repeat,number=number,globals=globals))

    print(f'{func}--{round(speed,4)} sec (ran{repeat*number:,}times)')

    return speed

if __name__=="__main__":
    get_time("doing(2,3)",repeat=10,number=5000)

