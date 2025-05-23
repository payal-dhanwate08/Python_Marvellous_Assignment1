def CheckEven(No):
    return(No % 2 == 0)

print("Enter the list:")
size = int(input())
data = list()
print("Enter element")
for i in range(size):
    no = int(input())
    data.append(no)

Fdata = list(filter(CheckEven,data))
print("Even number :",Fdata)