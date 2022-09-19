def po(a):
    c=co(a)
    e=0
    o=0
    for i in c:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e>0 and o>0:
        return "Mixed"
    elif e>0:
        return "Even"
    elif o>0:
        return "Odd"
def co(a):
    v=[]
    while a:
        d=a%10
        a=a//10
        v.append(d)
    return v

f=int(input())
print(po(f))