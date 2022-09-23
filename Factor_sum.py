def po(n):
    f=n.split(",")
    r=[]
    for i in f:
        p=int(i)
        c=fo(p)
        if str(c) in n:
            r.append(i)
    if len(r)>0:
        return sorted(r)
    else:
        r.append(-1)
        return sorted(r)
    
    
def fo(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=i
    return c
    
p=input()
print(*po(p))
