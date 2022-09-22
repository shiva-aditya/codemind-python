def po(n):
    c=[]
    for i in range(n-1,0,-1):
        if pal(i):
            c.append(i)
            break
    for j in range(n+1,n*n):
        if pal(j):
            c.append(j)
            break
    return c

def pal(i):
    d=str(i)
    a=d[::-1]
    if d==a:
        return True
    else:
        return False
    
    
o=int(input())
f=po(o)
d=[]
for i in f:
    d.append(abs(o-i))
if d[0]==d[1]:
    print(*f)
elif d[0]<d[1]:
    print(f[0])
else:
    print(f[1])