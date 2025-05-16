def main():
    print("Enter number")
    num = int(input())
    
    for i in range(1,num+1):
        for n in range(1,i+1):
            print(n,end=" ")
        print()
if __name__=="__main__":
     main()
   
