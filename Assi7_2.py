def Increse(No):
    return No*2
print("Enter the list:")
size = int(input())
data = list()
print("Enter element")
for i in range(size):
    no = int(input())
    data.append(no)

MData = list(map(Increse,data))
print("Doubled list :",MData)

