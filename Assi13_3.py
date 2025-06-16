class Numbers:
    def __init__(self,A):
        self.value=A
    def CheckPrime(self):
        if self.value>1:
            for i in range(2,self.value):
                if self.value%i==0:
                    print("The number is not prime")
                    break
            else:
                print("The number is prime")

    def CheckPerfect(self):
        if self.value==self.sumFactors():
            print("True")
        else:
            print("False")

    def sumFactors(self):
        self.sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                self.sum=self.sum+i
        print("sum of all factor of instance variable is:",self.sum)

    def Factor(self):
        for i in range(1,self.value):
            if self.value%i==0:
                print("The factor of value is:",i,)

def main():
    print("Enter number:")
    no=int(input())
    Obj1=Numbers(no)
    Obj1.CheckPrime()
    Obj1.CheckPerfect()
    Obj1.Factor()
    Obj1.sumFactors()

    Obj2=Numbers(no)
    Obj2.CheckPrime()
    Obj2.CheckPerfect()
    Obj2.Factor()
    Obj2.sumFactors()

if __name__=="__main__":
    main()

