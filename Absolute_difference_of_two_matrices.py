def po(n,m,t):
    ans=[]
    for i in range(t):
        d=[]
        for j in range(t):
            d.append(abs(n[i][j]-m[i][j]))
        ans.append(d)
    for i in ans:
        print(*i)





p=int(input())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
b=[]
for i in range(p):
    f=list(map(int,input().split()))
    b.append(f)
po(a,b,p)