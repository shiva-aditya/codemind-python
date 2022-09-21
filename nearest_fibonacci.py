def po(n):
    g=fo(n)
    h=[]
    e=[]
    for i in g:
        if (n-i)>0:
            h.append(n-i)
        else:
            e.append(abs(n-i))
    if h[-1]==e[0]:
        return [n-h[-1],n+e[0]]
    if h[-1]<e[0]:
        return [n-h[-1]]
    else:
        return [n+e[0]]
def fo(s):
    r=[0,1]
    for i in range(2,s):
        r.append(r[-1]+r[-2])
    return r

v=int(input())
p=po(v)
if len(p)==1:
    print(p[0])
else:
    for v in p:
        print(v,end=" ")