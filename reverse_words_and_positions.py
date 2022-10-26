def po(a):
    a=a[::-1]
    c=[]
    for i in a:
        c.append(i[::-1])
    return c





d=input()
d=d.split()
print(*po(d))