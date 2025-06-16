import os

def main():
    print("Enter the file name that you want to check:")
    fileName = input()

    ret = os.path.exists(fileName)

    if(ret == True):
        print("file is present in dirctory")

    else:
        print("There is no such file")

if __name__=="__main__":
    main()
