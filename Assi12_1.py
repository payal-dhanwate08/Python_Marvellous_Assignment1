class Demo:
    value = 101
    def __init__(self,A,B):
        self.No1=A
        self.No2=B

    def Fun(self):
        print("value of No1 is:",self.No1)
        print("value of No2 is:",self.No2)

    def Gun(self):
        print("value of No1 is:",self.No1)
        print("value of No2 is:",self.No2)

def main():
    obj1=Demo(11,21)
    obj2=Demo(51,10)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__=="__main__":
        main()
       

        

        