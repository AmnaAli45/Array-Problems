def searchPosition(arr,num):
    for i in range (len(arr)):
        if arr[i] >= num :
            return i
        
            
        

arr =[10,20,30,40,60]
num = int(input("Enter the number you want to insert in a sorted array: "))
print(searchPosition(arr,num))
