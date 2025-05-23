def area(no1,no2):
    result = no1 * no2
    return result

def perimeter(no1,no2):
    result = 2*(no1+no2)
    return result

def main():
    print("Enter lenght:")
    lenght = int(input())
    print("Enter width:")
    width = int(input())
    Ans = area(lenght,width)
    print("Area:",Ans)
    Ans = perimeter(lenght,width)
    print("perimeter:",Ans)

if __name__=="__main__":
    main()