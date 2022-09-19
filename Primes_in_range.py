import math
def po(a,b):
    v=[]
    for i in range(a,b+1):
        if i<1 or i==1:
            continue
        elif prime(i):
            v.append(i)
    return len(v)
def prime(b):
    d=int(math.sqrt(b))
    for j in range(2,d+1):
        if b%j==0:
            return False
    return True
i=int(input())
h=int(input())
print(po(i,h))