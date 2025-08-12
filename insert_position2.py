def searchPosition(arr,num):
    start = 0
    end=len(arr) - 1
    while (start <= end):
        mid = start + (end - start )//2
        if arr[mid] > num :
            end = mid -1
        elif arr[mid] < num :
            start = mid + 1
        else:
            return mid
    return end + 1




arr =[10,20,30,40,60]
num = int(input("Enter the number you want to insert in a sorted array: "))
print(searchPosition(arr,num))
