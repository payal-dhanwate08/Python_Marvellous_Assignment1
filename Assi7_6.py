def CheckPrime(No):
     if No>1:
        for i in range(2,No):
            if (No %i)==0:
                return False
        else:
                return True
        
Data=list()
print("Enter the list:")
size=int(input())

print("Enter element into list:")
for i in range(size):
    no=int(input())
    Data.append(no)
   
Fdata = list(filter(CheckPrime,Data))
print("filter Data :",Fdata)