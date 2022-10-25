import math
def po(a,k):
    c=0
    for i in range(len(a)):
        if prime(a[i]):
            if a[i]<=k:
                c+=1
    return c

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
e=int(input())
print(po(q,e))