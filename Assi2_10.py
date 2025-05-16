def main():
    print("Enter the number :")
    number = input()
    count = 0
    for i in number:
        count = count + int(i)
    print("Addition of digit is:",count)

if __name__=="__main__":
     main()
