### Multithreading
## When to use Multi Threading
### I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def fun1():
    for i in range(5):
        time.sleep(2)
        print("fun1 is running")

def fun2():
    for i in range(5):
        time.sleep(2)
        print("fun2 is running")
        
#creating thread
t1=threading.Thread(target=fun1) 
t2=threading.Thread(target=fun2)

start_time=time.time()

#starting thread
t1.start()
t2.start()

#wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()
print('execution time : ',(finished_time-start_time))