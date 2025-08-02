arr=[2,3,6,3,4,2,0,4,2,6,9,3,8]
arr2=[]

for i in arr:
    Find = False
    for j in arr2:
        if i == j:
            Find = True
            break
    if Find == False:
        arr2.append (i)

print (arr2)    