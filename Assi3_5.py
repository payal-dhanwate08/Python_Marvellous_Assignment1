import MarvellousNum

def listPrime():
    print("Number of elements :")
    size = int(input())
    
    Data = list()
    print("Enter the element into list")
    for i in range(size):
        no = int(input())
        Data.append(no)

    
    Ans = MarvellousNum.CheckPrime(no)
    sum = 0
    for num in Data:
        if MarvellousNum.CheckPrime(num):
            sum = sum+sum
        print("The sum is :",Ans)
    
if __name__=="__main__":
    listPrime()
    

