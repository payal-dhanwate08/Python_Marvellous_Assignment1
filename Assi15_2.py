import os

def main():
    print("Enter the file name that you want to read")
    fileName = input()

    ret = os.path.exists(fileName)

    if(ret==True):
        print("file is present in the directory")
        fobj=open(fileName,"r")
        data=fobj.read()

        print("data from file is :",data)

    else:
        print("There is no such file")

if __name__=="__main__":
    main()