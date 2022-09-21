import math
def po(a):
    if prime(a):
        if prime(co(a)):
            return "circular prime"
        else:
            return "prime but not a circular prime"
    else:
        return "not prime"

def co(u):
    c=[]
    while u:
        p=u%10
        u=u//10
        c.append(p)
    q=""
    for t in c:
        q=q+str(t)
    return int(q)
        
def prime(n):
    if n==1:
        return True
    g=int(math.sqrt(n))
    for i in range(2,g+1):
        if n%i==0:
            return False
    return True

g=int(input())
print(po(g))