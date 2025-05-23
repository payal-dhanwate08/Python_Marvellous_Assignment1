def CheckPrime(no):
    if no>1:
        for i in range(2,no):
            if (no %i)==0:
                print("it is not a prime number")
                break
       
        else:
             print("it is prime number")
               
def main():
    print("Enter a number:")
    num = int(input())

    CheckPrime(num)

if __name__=="__main__":
    main()








    