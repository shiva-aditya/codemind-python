def po(b):
    a=b
    c=[]
    while a:
        d=a%10
        a=a//10
        c.append(d)
    c.reverse()
    t=0
    for i in range(0,len(c)):
        t=t+c[i]**(i+1)
    return t==b

g=int(input())
print(po(g))