def po(a):
    e=[]
    o=[]
    for i in range(len(a)):
        if a[i]%2==0:
            e.append(a[i])
        else:
            o.append(a[i])
    c=[]
    if len(e)<len(o):
        for i in range(len(e)):
            c.append(e[i])
            c.append(o[i])
        q=len(o)-len(e)
        for i in range(len(o)-q,len(o)):
            c.append(o[i])
        if q%2!=0:
            c.append(0)
    elif len(e)>len(o):
        for i in range(len(o)):
            c.append(e[i])
            c.append(o[i])
        q=len(e)-len(o)
        for i in range(len(e)-q,len(e)):
            c.append(e[i])
        if q%2!=0:
            c.append(0)
    else:
        for i in range(len(o)):
            c.append(e[i])
            c.append(o[i])
    return c
    
s=int(input())
q=list(map(int,input().split()))
print(*po(q))