arr=[2,3,7,10,45,9]

target=int(input("Enter the value you want to search from array: "))
found = False
for i in arr :
    if target == i:
        found = True
        break

if (found):
    print ("Target is found ")
else:
   print ("Target not found ") 
