"""
import threading
import time

#startthread takes a name and prints it counter no. of times
def start_thread(name,counter):
    for i in range(counter):
        print(name, i+1,sep=':')
        time.sleep(1)

if __name__=="__main__":
    start_thread("Ash",5)
    start_thread("Aryan",10)
"""

# THE ABOVE CODE IS NOT OF THREADING. IT IS MORE OF SLEEP METHOD THE BELOW CODE IS OF THREADING
import threading
import time

#task to be done by thread
#startthread takes a name and prints it counter no. of times
def start_thread(name,counter):
    for i in range(counter):
        print(name, i+1,sep=':')
        time.sleep(1)

if __name__=="__main__":
    #thread creation
    thread_one=threading.Thread(target=start_thread, args=("Thread1",5))
    thread_two=threading.Thread(target=start_thread, args=("Thread2",10))

    #thread calling
    print("starting thread 1")
    thread_one.start()
    time.sleep(3)
    #due to sleep thread 2 got time to run
    print("starting thread 2")
    thread_two.start()
