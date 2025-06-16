class BookStore:
    NoOfBooks=0
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print("The name of book is:"+self.Name)
        print("The name of Author is:"+self.Author)
        print("The number of books is:",BookStore.NoOfBooks)

def main():
    print("Enter book name:")
    Name1=input()
    print("Enter Author name:")
    Author1=input()
    Obj1 = BookStore(Name1,Author1)
    Obj1.Display()

    print("Enter book name:")
    Name2=input()
    print("Enter Author name:")
    Author2=input()

    Obj2=BookStore(Name2,Author2)
    Obj2.Display()
       

if __name__=="__main__":
    main()
    
   
