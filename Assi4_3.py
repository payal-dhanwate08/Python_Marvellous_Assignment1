from functools import reduce

def CheckNum(No):
    return No>=70 and No<=90

def Increse(No):
    return No+10

def product(No1,No2):
    return No1*No2

print("Enter the size of list")
size = int(input())
data = list()
print("Enter the values:")
for i in range(size):
    no = int(input())
    data.append(no)


Fdata = list(filter(CheckNum,data))
print("filter Data :",Fdata)

MData = list(map(Increse,Fdata))
print("map Data :",MData)

RData = reduce(product,MData)
print("reduce Data :",RData)