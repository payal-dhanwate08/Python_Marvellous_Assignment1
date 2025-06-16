import threading

def Small(ch):
    count=0
    for i in ch:
        if i.islower():
            count=count+1

    print("The number of small letter in string is :",count)
    print("Thred ID of thred is :",threading.get_ident())
    print("The name of current thred is :",threading.current_thread())
    
def Capital(ch):
    count=0
    for i in ch:
        if i.isupper():
            count=count+1

    print("The number of capital letter in string is :",count)
    print("Thred ID of thred is :",threading.get_ident())
    print("The name of current thred is :",threading.current_thread())


def Digit(ch):
    count=0
    for i in ch:
        if i.isdigit():
            count=count+1

    print("The digits in string is :",count)
    print("Thred ID of thred is :",threading.get_ident())
    print("The name of current thred is :",threading.current_thread())

def main():
    print("Enter input :")
    strr=input()

    T1=threading.Thread(target=Small,args=(strr,))
    T2=threading.Thread(target=Capital,args=(strr,))
    T3=threading.Thread(target=Digit,args=(strr,))

    T1.start()
    T2.start()
    T3.start()

if __name__=="__main__":
    main()