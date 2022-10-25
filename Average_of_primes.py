import math
def po(a,l):
    c=[]
    for i in range(l):
        if prime(a[i]):
            c.append(a[i])
    e=sum(c)/len(c)
    print("{:0.2f}".format(e))

def prime(n):
    if n<=1:
        return False
    d=int(math.sqrt(n))
    for i in range(2,d+1):
        if n%i==0:
            return False
    return True
    
s=int(input())
q=list(map(int,input().split()))
po(q,s)