import math
def po(n):
    c=0
    h=n.index(max(n))
    m=n.index(min(n))
    if h>m:
        for i in range(m,h+1):
            if prime(n[i]):
                c+=1
    else:
        for i in range(m,h-1,-1):
            if prime(n[i]):
                c+=1
    return c
    
    
    
def prime(n):
    if n==1 or n<0:
        return False
    t=int(math.sqrt(n))
    for i in range(2,t+1):
        if n%i==0:
            return False
    return True
    
    
t=int(input())   
u=list(map(int,input().split()))
print(po(u))
    