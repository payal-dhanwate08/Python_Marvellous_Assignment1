from functools import reduce

def product(No1,No2):
     return No1*No2

print("Enter the list:")
size = int(input())
data = list()
print("Enter element")
for i in range(size):
    no = int(input())
    data.append(no)

RData = reduce(product,data)
print("product :",RData)