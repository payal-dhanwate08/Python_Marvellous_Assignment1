import threading

def thread1():
    for i in range(1,51):
        print(i)

def thread2():
    for i in range(50,0,-1):
        print(i)

def main():
    T1=threading.Thread(target=thread1)
    T1.start()
    T1.join()
    T2=threading.Thread(target=thread2)
    T2.start()
    T2.join()

if __name__=="__main__":
    main()