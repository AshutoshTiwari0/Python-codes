import time
import threading

semaphore=threading.Semaphore(5)

def process(id):
    semaphore.acquire()
    print(f"{id} is running")
    time.sleep(5)
    print(f"{id} is finished")
    semaphore.release()



if __name__=="__main__":
    for i in range(10):
        time.sleep(0.5)
        thread=threading.Thread(target=process,kwargs={'id':i+1})
        thread.start()
