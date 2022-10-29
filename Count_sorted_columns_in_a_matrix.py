def po(n):
    ans=[]
    for i in range(len(n[0])):
        d=[]
        for j in n:
            d.append(j[i])
        ans.append(d)
    c=0
    for i in ans:
        e=sorted(i)
        if i==e or e[::-1]==i:
            c+=1
    return c
        
p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
print(po(a))