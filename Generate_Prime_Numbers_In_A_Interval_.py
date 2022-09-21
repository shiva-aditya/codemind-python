import math as m
def po(a,b):
    f=[]
    for i in range(a,b+1):
        if prime(i):
            f.append(i)
    return f
def prime(t):
    if t==1:
        return False
    g=int(m.sqrt(t))
    for i in range(2,g+1):
        if t%i==0:
            return False
    return True
a=int(input())
b=int(input())
f=po(a,b)
for k in f:
    print(k)