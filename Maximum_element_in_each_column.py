def po(a,r,c):
    f=[]
    for i in range(c): 
        t=[]
        while i<len(a):
            t.append(a[i])
            i+=c
        f.append(max(t))
    return f

r,c=list(map(int,input().split()))
d=[]
for _ in  range(r):
    d=d+list(map(int,input().split()))
u=po(d,r,c)
for i in u:
    print(i)