import threading

def Evenlist(data):
    sum=0
    for i in data:
        if i % 2==0:
            sum = sum+i
    print("The even element sum is:",sum)

def Oddlist(data):
    Oddsum=0
    for i in data:
        if i %2!=0:
            Oddsum=Oddsum+i
    print("The odd element sum is:",Oddsum)

def main():
    data=list()
    print("Enter size of list:")
    size=int(input())

    print("Enter element into list:")
    for i in range(size):
        no = int(input())
        data.append(no)

    T1=threading.Thread(target=Evenlist,args=(data,))
    T2=threading.Thread(target=Oddlist,args=(data,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__=="__main__":
    main()
