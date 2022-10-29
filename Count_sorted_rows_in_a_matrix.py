def po(n):
    c=0
    for i in n:
        e=sorted(i)
        if e==i or e[::-1]==i:
            c+=1
    return c





p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
print(po(a))