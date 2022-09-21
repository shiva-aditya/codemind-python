import math
def po(a):
    f=[]
    for i in range(a,0,-1):
        if prime(i):
            f.append(i)
            break
    for j in range(a+1,a*a):
        if prime(j):
            f.append(j)
            break
    n=abs(a-f[0])
    m=abs(a-f[1])
    if n<m:
        return f[0]
    elif n==m:
        return f[0]
    else:
        return f[1]
def prime(f):
    g=int(math.sqrt(f))
    for v in range(2,g+1):
        if f%v==0:
            return False
    return True

for _ in range(int(input())):
    d=int(input())
    print(po(d))