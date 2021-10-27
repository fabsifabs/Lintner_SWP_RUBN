

def sumIte(i):
    x = i
    while i > 0:
        x = x+(i-1)
        i = i-1
    return x

def sumRec(i):
    if i == 1:
        return 1

    return i + sumRec(i-1)
    

def powInt(i,x):
    res = i
    for _ in range(1,x):
        res *= i
    return res

def powRec(i , x):
    if x == 0:
        return 1
    elif x == 1:
        return i
    else:
        return i * powRec(i, x-1)

print(powRec(4,2))