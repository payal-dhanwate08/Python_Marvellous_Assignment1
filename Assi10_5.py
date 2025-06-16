from functools import reduce

def CheckPrime(No):
     if No>1:
        for i in range(2,No):
            if (No %i)==0:
                return False
        else:
            return True
                      
def product(No):
     return No*2
   
def maximum(X,Y):
    if X>Y:
        return X
    else:
        return Y
    
Data=list()
print("Enter size of list:")
size=int(input())

print("Enter element into list:")
for i in range(size):
    no=int(input())
    Data.append(no)
   
Fdata = list(filter(CheckPrime,Data))
print("filter Data :",Fdata)

MData = list(map(product,Fdata))
print("map Data :",MData)

RData = reduce(maximum,MData)
print("reduce Data :",RData)