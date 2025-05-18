def main():
    print("Number of elements:")
    size = int(input())

    Data=list()
    print("Enter the number of list")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    max_element = Data[0]
    for i in Data:
        if i>max_element:
            max_element= i

    print("maximum number is:",max_element)

if __name__=="__main__":
     main()
    