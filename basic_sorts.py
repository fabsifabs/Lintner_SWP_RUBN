import random 
 
arr = []


for x in range(100):
    arr.append(random.randrange(100))

for x in range(len(arr)-1):
    for y in range(0, (len(arr)-1)-x):
        if arr[y]>arr[y+1]:
            arr[y],arr[y+1] = arr[y+1],arr[y]



print(*arr)

