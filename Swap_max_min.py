arr=[]
n = int (input("Enter the size of array: "))

for i in range (n):
    value = eval (input("Enter the values of array: "))
    arr.append(value)

print ("-----------------------Before swapping: ")
print(arr)

max=arr[0]
min=arr[0]

p,q=0,0
for i in range (n):
    if max < arr[i]:
        max=arr[i]
        p=i

for i in range (n):
    if min > arr[i]:
        min=arr[i]
        q=i

arr[p], arr[q] = arr[q], arr[p]
print ("-----------------------After swapping: ")
print(arr)
