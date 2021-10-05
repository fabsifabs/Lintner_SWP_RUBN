arr = [0,1,2,3,4,5,6,7,8,9,10,11]
#print (len(arr))
n = 2

""""
b = False

for x in arr:
    if x == n:
        print("on place ",x," is the number" )
        b = True
        break
    else: 
        print("on place ",x, "is not the number")
        b = False

if b == False:
    print(n, "was not in the array")
"""


e = len(arr)#current number
s = 0  #start from current field
m = 0  #mid from current field
r = 0 #runthroo

while s <= e :
    m = int((s+e)/2)
    r = r+1

    if  n == arr[m]:
        print ("Stelle im Array: ",m, " Durchläufe: ", r)
    elif n < arr[m]:
        e = m -1
    else:
        s = m +1 

if s<e :
    print("Die gesuchte Zal ist nicht enthalten!")


     

