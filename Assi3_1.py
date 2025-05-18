def main():
    print("Number of elements:")
    size = int(input())

    Data=list()
    print("Enter the number of list")
    
    for i in range(size):
        no = int(input())
        Data.append(no)
    

    sum = 0
    for i in Data:
        sum = sum + i
    print("Addition is :",sum)

if __name__=="__main__":
     main()