# we want first our thread to finish and then next one should execute

#lock ensures that one thread runs only.

import threading
import time

#creating a lock
lock=threading.Lock()

def counter(name, count):
    for i in range(count):
        time.sleep(2)
        print(name, i , sep='||')



# implementing  a lock
def task1():
    lock.acquire() # lock start jab tak ye thread nhi popora hota it will keep on running and then go to next thread
    counter('t-1', 5)
    lock.release() # releases the lock so that next thread can run

def task2():
    lock.acquire()
    counter('t-2',5)
    lock.release()

def task3():
    lock.acquire()
    counter('t-3',5)
    lock.release()

def task4():
    lock.acquire()
    counter('t-4',5)
    lock.release()

def main():
    thread1=threading.Thread(target=task1)
    thread2=threading.Thread(target=task2)
    thread3=threading.Thread(target=task3)

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
    thread3.start()
    thread3.join()
    

    """
    thread1.join()
    thread2.join()
    """
if __name__=="__main__":
    main()