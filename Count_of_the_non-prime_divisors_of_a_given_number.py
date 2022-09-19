import math
def po(n):
    c=[]
    for i in range(1,n+1):
        if n%i==0:
            if prime(i):
                continue
            c.append(i)
    return len(c)
def prime(i):
    if i==1:
        return False
    g=int(math.sqrt(i))
    for u in range(2,g+1):
        if i%u==0:
            return False
    return True
    
p=int(input())
print(po(p))