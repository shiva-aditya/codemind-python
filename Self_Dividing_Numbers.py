def po(a,b):
    f=[]
    for i in range(a,b+1):
        if mo(i):
            f.append(i)
    return f
def mo(e):
    if e%10==0:
        return False
    p=e
    g=[]
    while p:
        t=p%10
        p=p//10
        if t==0:
            continue
        else:
            g.append(t)
    for k in g:
        if e%k!=0:
            return False
    return True
h=int(input())
y=int(input())
print(*(po(h,y)))