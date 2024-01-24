from time import perf_counter
from functools import wraps
from datetime import datetime


def get_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        s=perf_counter()
        func(*args,**kwargs)
        e=perf_counter()
        print("time taken is "+str(e-s)+"seconds")

    return wrapper

def timestamp()->str:
    return f"{datetime.now() : %H:%M:%S}"


def killtime():
    for i in range(10**8):
        pass
