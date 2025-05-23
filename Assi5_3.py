def checkAge():
    print("Enter age:")
    Age = int(input())

    if(Age>=18):
        print("Eligible to vote")
    else:
        print("not Eligible")

if __name__=="__main__":
    checkAge()