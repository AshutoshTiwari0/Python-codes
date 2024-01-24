import multiprocessing as mp
import timewaste
from timewaste import get_time , timestamp, killtime
import os

def func(param):
    print(f"starting {mp.current_process().name} ({os.getpid()}  {timestamp()})")
    killtime()
    print(f"{os.getpid()} finished! ({timestamp})")


@get_time
def main():
    # creating a process
    process1=mp.Process(name="first process",target=func, args=('sample1',))
    process2=mp.Process(name="second process",target=func, args=('sample2',))


    #starting a process
    #both will start at same time
    process1.start()
    process2.start()

    #joining process
    process1.join()
    process2.join()


if __name__=="__main__":
    main()

