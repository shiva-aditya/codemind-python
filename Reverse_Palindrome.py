def po(a):
    v=co(a)
    d=""
    for _ in v:
        d=d+str(int(_))
    a=a+int(d)
    if mo(a):
        return a
    else:
        return po(a)
def mo(a):
    v=co(a)
    f=v[::-1]
    if v==f:
        return True
    else:
        return False
def co(a):
    v=[]
    while a:
        d=a%10
        a=a//10
        v.append(d)
    return v
v=int(input())
print(po(v))