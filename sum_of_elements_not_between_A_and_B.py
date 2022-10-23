def po(a,p,q,l):
    a.sort()
    if p not in a or q not in a:
        if p not in a and q not in a:
            return 0
        elif p not in a:
            a.insert(0,p)
        else:
            a.append(q)
    return fo(a,p,q)
def fo(a,p,q):
    a.sort()
    s=sum(a)
    r=a.index(p)
    w=a.index(q)
    z=a[r:w+1:]
    for i in z:
        s-=i
    return s
        
s=int(input())
p=list(map(int,input().split()))
a,b=map(int,input().split())
print(po(p,a,b,s))