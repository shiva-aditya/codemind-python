import math
def po(x):
    if prime(x):
        return 0
    else:
        h=[]
        for i in range(x,0,-1):
            if prime(i):
                h.append(i)
                break
        for j in range(x,x*x):
            if prime(j):
                h.append(j)
                break
        if (x-h[0])<(h[1]-x):
            return x-h[0]
        else:
            return h[1]-x
def prime(a):
    if a==1:
        return False
    r=int(math.sqrt(a))
    for i in range(2,r+1):
        if a%i==0:
            return False
    return True

a=int(input())
print(po(a))