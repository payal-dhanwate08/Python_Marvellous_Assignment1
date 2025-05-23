def Vowel():
    print("Enter the charecter:")
    char = input()
    if char =='a' or char =='e' or char =='i' or char =='o' or char =='u':
        print("is Vowel",char)
    else:
        print("is consonant",char)

if __name__=="__main__":
    Vowel()