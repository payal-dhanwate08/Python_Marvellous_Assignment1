import Arithmatic

def main():
    print("Enter first number :")
    value1 = int(input())
    print("Enter second number :")
    value2 = int(input())
    Ans1 = Arithmatic.Add(value1,value2)
    print("Addition is:",Ans1)
    Ans2 = Arithmatic.sub(value1,value2)
    print("subtraction is :",Ans2)
    Ans3 = Arithmatic.mult(value1,value2)
    print("Multiplication is :",Ans3)
    Ans4 = Arithmatic.div(value1,value2)
    print("Division is :",Ans4)

if __name__=="__main__":
    main()

