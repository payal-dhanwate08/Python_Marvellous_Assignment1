def largeNo():
    print("Enter 5 number :")
    no1 = int(input())
    no2 = int(input())
    no3 = int(input())
    no4 = int(input())
    no5 = int(input())

    large=no1

    if no2>large:
        large=no1
    if no3>large:
        large=no3
    if no4>large:
        large=no4
    if no5>large:
        large=no5
    print("Maximum number :",large)

if __name__=="__main__":
    largeNo()
















