class Arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        print("Enter first value")
        self.value1=int(input())
        print("Enter second value")
        self.value2=int(input())

    def Addition(self):
         return self.value1+self.value2
         
    def Subtraction(self):
        return self.value1-self.value2
    
    def Multiplication(self):
       return self.value1*self.value2
    
    def Division(self):
       return self.value1/self.value2
    
def main():

    obj1=Arithmatic()
    obj1.Accept()
    print("Addition is:",obj1.Addition())
    print("Subtraction is:",obj1.Subtraction())
    print("Multiplication is:",obj1.Multiplication())
    print("Division is:",obj1.Division())

    obj2=Arithmatic()
    obj2.Accept()
    print("Addition is:",obj2.Addition())
    print("Subtraction is:",obj2.Subtraction())
    print("Multiplication is:",obj2.Multiplication())
    print("Division is:",obj2.Division())

   
if __name__=="__main__":
    main()



        