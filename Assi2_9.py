def Digits():
    print("Enter number")
    num = input()
    count=0
    for i in range(len(num)):
        count=count+1
    print(count)

if __name__=="__main__":
     Digits()