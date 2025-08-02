arr1=[]
n = int (input("Enter the size of first array: "))

for i in range (n):
    value = eval (input("Enter the values of first array: "))
    arr1.append(value)

arr2=[]
n = int (input("Enter the size of second array: "))

for i in range (n):
    value = eval (input("Enter the values of second array: "))
    arr2.append(value)

print("---------- First Array ------------")
print(arr1)
print("---------- Second Array ------------")
print(arr2)
print("---------- Intersection of Arrays -----------")
for i in arr1:
    for j in arr2:
        if i == j:
            print (i)
            break