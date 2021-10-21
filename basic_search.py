import time

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


def interative_search():
    b = False
    d = 0
    t = time.time_ns()
    for x in arr:
        if x == n:

            d +=1
            print("Die Zahl:",n," steh im Array an Stelle: ",x, " Es brauchte ", d," Durchlaufe" )
            b = True
            print("Durchlaufe benoetigt:",d)
            print("Zeit fuer die suche benoetigt:",time.time_ns()-t)
            break

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
            print ("Die Zahl:",n," steh im Array an Stelle: ",m, " Es brauchte ", r," Durchlaufe")
            print("Zeit fuer die suche benoetigt:",time.time_ns()-t)
            return 
        elif n < arr[m]:
            e = m - 1
        elif n > arr[m]:
            s = m + 1 

    print("Die gesuchte Zahl ist nicht enthalten!")
#print (type(arr))
print ("Interativ oder binaer? (tippe I/B)")
i = input()
if i == "B":
    print("Gesuchte Zahl:")
    n = int(input())
    binari_search()  
elif  i == "I"  :
    print("Gesuchte Zahl:")
    n = int(input())
    interative_search()
else: 
    print("KEINE GÜLTIGE EINGABE!!!")