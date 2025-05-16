def factors():
    print("Enter the number")
    n = int(input())
    sum=0
    for i in range(1,n):
        if n % i == 0:
            sum=sum+i
    print("The sum is :",sum)

if __name__=="__main__":
    factors()