def largeNo(x,y,z):
    if(x>y):
        print("largest number is:",x)
    elif(y>x):
        print("largest number is:",y)
    else:
        print("largest number is:",z)

def main():
    print("Enter the number :")
    no1 = int(input())
    no2 = int(input())
    no3 = int(input())

    largeNo(no1,no2,no3)

if __name__=="__main__":
    main()

