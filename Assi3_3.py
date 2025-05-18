def main():
    print("Number of elements:")
    size = int(input())
    Data = list()
    print("Enter the numbers of list")
    for i in range(size):
        no = int(input())
        Data.append(no)

    min_element = Data[0]
    for i in Data:
        if i<min_element:
            min_element= i
            

    print("minimum number is :",min_element)

if __name__=="__main__":
     main()
