import math
def po(a):
    c=[]
    for i in range(2,a):
        if a%i==0:
            if prime(i):
                c.append(i)
    return c
    
    
def prime(a):
    y=int(math.sqrt(a))
    for i in range(2,y+1):
        if a%i==0:
            return False
    return True
    
e=int(input())
p=po(e)
if len(p)>=2:
    print(*(p))
else:
    print(-1)