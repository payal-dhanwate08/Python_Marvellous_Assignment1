def main():
    print("Enter the value of N ")
    N = int(input())
    fact = 1
    for i in range(1,N+1):
        fact = fact*i
    print("factorial is :",fact)

if __name__=="__main__":
     main()
       