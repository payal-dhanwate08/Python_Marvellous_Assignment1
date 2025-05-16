def fun():
    print("Enter number")
    no = int(input())
    for i in range(no): 
        for num in range(1,no+1):
            print(num   ,end=" ")
        print()
          
if __name__ =="__main__":
    fun()