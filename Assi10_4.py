from functools import reduce

def EvenNo(No):
     return(No % 2 == 0)
    
def Square(No):
    return No**2

def sum(No1,No2):
    return No1+No2

print("Enter the size of list")
size = int(input())
data = list()
print("Enter the values:")
for i in range(size):
    no = int(input())
    data.append(no)

Fdata = list(filter(EvenNo,data))
print("filter Data :",Fdata)

MData = list(map(Square,Fdata))
print("map Data :",MData)

RData = reduce(sum,MData)
print("reduce Data :",RData)