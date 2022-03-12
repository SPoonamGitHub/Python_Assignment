import threading

def THREAD1():
    for i in range(51):
        print(i)
def THREAD2():
    for i in range(50,-1,-1):
        print(i)

if __name__ == "__main__":

    thread1 = threading.Thread(target=THREAD1, args=())
    thread2 = threading.Thread(target=THREAD2, args=())

    thread1.start()
    thread1.join()
    thread2.start()
	 #thread2.join()