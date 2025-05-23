def Addition(no1,no2):
    result = no1 + no2
    return result

def Difference(no1,no2):
    result = no1 - no2
    return result

def Product(no1,no2):
    result = no1 * no2
    return result

def Division(no1,no2):
    result = no1 / no2
    return result

def main():
    print("Enter first number :")
    value1 = int(input())
    print("Enter second number :")
    value2 = int(input())

    Ans = Addition(value1,value2)
    print("sum:",Ans)

    Ans = Difference(value1,value2)
    print("Difference:",Ans)

    Ans = Product(value1,value2)
    print("Product:",Ans)

    Ans = Division(value1,value2)
    print("Division:",Ans)

if __name__=="__main__":
    main()