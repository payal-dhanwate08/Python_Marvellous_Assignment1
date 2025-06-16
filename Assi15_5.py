import sys

def main():
    print("Enter file name:")
    filename = input()
    print("Enter srting:")
    str = input()

    fobj = open(filename,"r")
    data = fobj.read()

    count = data.count(str)

    print(count)

if __name__=="__main__":
    main()

