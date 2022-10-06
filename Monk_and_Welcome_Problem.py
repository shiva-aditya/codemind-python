def po(n,m,p):
    c=[]
    for i in range(0,p):
        c.append(a[i]+b[i])
    return c



d=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*po(a,b,d))