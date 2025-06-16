import threading
def Even():
    for i in range(0,21,2):
        print(i)

def Odd():
    for i in range(1,21,2):
        print(i)

def Addition():
    T1=threading.Thread(target=Even)
    T1.start()
    T1.join()
    T2=threading.Thread(target=Odd)
    T2.start()
    T2.join()

if __name__=="__main__":
    Addition()