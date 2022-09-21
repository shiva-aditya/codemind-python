def mo(a):
    c=[]
    while a:
        d=a%10
        a=a//10
        c.append(d)
    p=1
    x=0
    for i in c:
        p=p*i
        x=x+i
    return abs(p-x)
p=int(input())
print(mo(p))