def pattern(no):
    for i in range(1,no+1):
        for j in range(i,no+1):
            print(" * " *j)
            break

def main():
    print("Enter number:")
    num = int(input())
    pattern(num)

if __name__=="__main__":
    main()