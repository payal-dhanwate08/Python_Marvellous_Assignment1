def main():
    print("Number of elements :")
    size = int(input())

    Data = list()
    print("Enter no of list")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Element to search")
    n=int(input())
    count=0
    for i in Data:
        if i == n:
            count=count+1
    print("frequncy of number is :",count)

main()