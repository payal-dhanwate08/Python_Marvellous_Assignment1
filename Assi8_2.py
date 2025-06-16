import threading
def evenfactor(no):
    
    Esum=0
    for i in range(1,no):
        if no%i==0 and i%2==0:
            Esum=Esum+i
    print("The evenfactor sum is:",Esum)

def Oddfactor(no):

    Osum=0
    for i in range(1,no):
        if no%i==0 and i%2!=0:
            Osum=Osum+i
    print("The oddfactor sum is:",Osum)

def main():
    print("Enter number:")
    no1 = int(input())

    T1 = threading.Thread(target=evenfactor,args=(no1,))
    T1.start()
    T1.join()

    T2 = threading.Thread(target=Oddfactor,args=(no1,))
    T2.start()
    T2.join()
    
    print("Exit from main")

if __name__=="__main__":
    main()