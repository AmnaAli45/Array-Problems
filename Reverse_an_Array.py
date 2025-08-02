
size = int (input("Enter the size of  an array: "))
arr= []
for i in range (size):
    value = int (input("Enter the value of array: "))
    arr.append(value)

print("-----------Original Array------------")
print(arr)

#array reversing by using two pointer approach
start=0
end=size-1

while start < end :
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -=1

print("-----------Reversed Array------------")
print(arr)

