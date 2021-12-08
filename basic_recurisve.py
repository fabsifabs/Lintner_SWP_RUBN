import math
import time


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

def sumEnd(i):
    return sum(0,i)

def sum(h,i):
    if i == 0:
        return h
    return sum(h+i, i-1)

def fakIte(i):
    x = 1
    while i > 1: 
        x = x*(i)
        i = i-1
    return x

def fakRec(i):
    if i == 1:
        return 1
    return i * fakRec(i-1)
    
def fakEnd(i):
    return fak(1,i)

def fak(h,i):
    if i<=1:
        return h
    return fak(h*i,i-1)

def powIte(i,x):
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

def powEnd(i,x):
    return pow(1,i,x)

def pow(h,i,x):
    if x == 0:
        return h
    return(pow(h*i,i,x-1))

b =time.perf_counter_ns()
print("sumIte:",sumIte(400))
t1=time.perf_counter_ns()-b
print("Time sumIte:", t1 ,"ns")
b =time.perf_counter_ns()
print("sumRec:",sumRec(400))
t2=time.perf_counter_ns()-b
print("Time sumRec:", t2 ,"ns")
b =time.perf_counter_ns()
print("sumEnd:",sumEnd(400))
t3=time.perf_counter_ns()-b
print("Time sumEnd:", t3 ,"ns")``

print("Ite:", t1,"ns", "    Rec: ", t2-t1, "ns", "  End: ",t2-t3, "ns" )

#print(fakIte(300),"\n",fakRec(300),"\n",fakEnd(300))

#print(powIte(30,3),"\n",powRec(30,3),"\n",powEnd(30,3))