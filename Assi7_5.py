def palindrome():
    print("Enter a string:")
    name=input()
    reversed_string=name[::-1]
    if name==reversed_string:
        print(name,"is a palindrome")
    else:
        print(name,"is not palindrome")

if __name__=="__main__":
    palindrome()
    