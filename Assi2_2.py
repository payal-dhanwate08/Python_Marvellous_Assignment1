def fun():
    print("Enter number")
    num = int(input())
    i = 0

    while(i<num):
         print("*   "*num)
         i = i+1
        
if __name__ =="__main__":
    fun()