import time

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print("Zahl:")
n = int(input())
print("zahl:",n)

def interative_search():
    b = False
    d = 0
    for x in arr:
        if x == n:

            d +=1
            print("on place ",x," is the number" )
            b = True
            print("Durchlaufe benoetigt:",d)
            break
        else: 
            #print("on place ",x, "is not the number")
            b = False

    if b == False:
        print(n, "was not in the array")


def  binari_search():
    e = len(arr) -1#current number
    s = 0  #start from current field
    m = 0  #mid from current field
    r = 0 #runthroo
    t = time.time_ns()

    while s <= e :
        m = int((s+e)/2)
        r = r+1

        if  n == arr[m]:
            print ("Stelle im Array: ",m, " Durchlaeufe: ", r)
            print("Zeit benoetigt:",time.time_ns()-t)
            return 
        elif n < arr[m]:
            e = m - 1
        elif n > arr[m]:
            s = m + 1 

    
    print("Die gesuchte Zahl ist nicht enthalten!")


binari_search()    
#interative_search()