import sys

def main():

    file1=sys.argv[1]
    fobj = open(file1,"r")
    data1 = fobj.read()

    file2=sys.argv[2]
    fobj = open(file2,"r")
    data2 = fobj.read()

    if(data1 == data2):
        print("success")

    else:
        print("failure")

if __name__=="__main__":
    main()
