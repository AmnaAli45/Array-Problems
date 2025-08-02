arr=[]
n = int (input("Enter the size of array: "))

for i in range (n):
    value = eval (input("Enter the values of array: "))
    arr.append(value)

print("----------Array Elemnts-------------")
for i in arr:
    print (i)
