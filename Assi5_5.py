def CheckNum(no):
    if(no%2==0):
        print("is an even number")
    else:
        print("is an odd number")

def main():
    print("Enter a number:")
    num = int(input())
    CheckNum(num)

if __name__=="__main__":
    main()
