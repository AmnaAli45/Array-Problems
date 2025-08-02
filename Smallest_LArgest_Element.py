arr=[]
n = int (input("Enter the size of array: "))

for i in range (n):
    value = eval (input("Enter the values of array: "))
    arr.append(value)

# Smallest Element
small=arr[0]
for i in arr:
    if small > i:
        small=i

print ("-------------Smallest Element-----------")
print(small)

# largest Element
large=arr[0]
for i in arr:
    if large < i:
        large=i

print ("-------------Largest Element-----------")
print(large)
