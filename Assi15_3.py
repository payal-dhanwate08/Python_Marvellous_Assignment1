import sys

def main():

    fileName = sys.argv[1]

    fobj = open(fileName,"r")
    data = fobj.read()

    fobj = open("Demo.txt","w")
    newData = fobj.write(data)


    print("data Succesfully copied ")

if __name__=="__main__":
    main()