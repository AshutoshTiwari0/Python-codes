import multiprocessing as mp
from timewaste import get_time
import time

def convert_to_x(num:int):
    time.sleep(2)
    return num * 'x'

@get_time
def main():
    print("cores available"+str(mp.cpu_count()))

    values=tuple(range(1,13))

    with mp.Pool() as pool:
        results=pool.map(convert_to_x, values)
        print("output is "+str(results))



if __name__=="__main__":
    main()

