import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def a():
    print("a waiting for lock 1")
    lock1.acquire()
    print("a acquired  lock 1")
    print("Inside critical section of a, acquired lock 1")
    c()
    lock1.release()

def b():
    print("b waitinglock1.acquire() for lock 1")

    print("b acquired  lock 1")
    print("Inside critical section of b, acquired lock 1")
    lock1.release()


def c():
    print("c waiting for lock 2")
    lock2.acquire()
    print("c acquired  lock 2")
    print("Inside critical section of c, acquired lock 2")
    b()
    lock2.release()



t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)
t1.start()
t1.join()

t2.start()
t2.join()





# https://vt/analysis/www.amazon.com/products










