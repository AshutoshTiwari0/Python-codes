
from functools import wraps
from time import perf_counter,sleep

def get_time(func):
    """tells time for execution"""
    print("i ran")

    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time=perf_counter()
        func(*args,**kwargs)
        end_time=perf_counter()
        time_taken=end_time-start_time
        print(f"total time is {time_taken}")

    return wrapper

@get_time  # due to this decorator our function get_time on line 4 will run due to which our wrapper will run and we will get the execution time
def do_some(parameter):
    """doing something"""
    print(" i ran after decorator heheh")
    sleep(1)
    print(parameter)

if __name__=="__main__":
    do_some("attention")

    