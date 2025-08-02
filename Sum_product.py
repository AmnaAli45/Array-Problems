arr=[]
n = int (input("Enter the size of array: "))

for i in range (n):
    value = eval (input("Enter the values of array: "))
    arr.append(value)

sum =0
prod = 1
for i in arr:
    sum += i
    prod *= i

print (f"Sum of array elemnts is: {sum}")
print (f"Product of array elemnts is: {prod}")