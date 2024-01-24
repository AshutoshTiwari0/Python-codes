#when two threads access same variable at same time
import threading
import time

lock=threading.Lock()
def edit(operation, amount, repeat):
    global value

    lock.acquire()
    for _ in range(repeat):
        temp=value
        time.sleep(0)
        if operation=="add":
            temp=temp+amount

        elif operation=="sub":
            temp=temp-amount

        time.sleep(0)
        value=temp

    lock.release()

if __name__=="__main__":
    value=0
    add=threading.Thread(target=edit,args=("add",100,1400))
    sub=threading.Thread(target=edit,args=("sub",100,1400))

    add.start()
    sub.start()

    print("waiting to finish")
    add.join()
    sub.join()

    print(value)
