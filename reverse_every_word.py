def po(a):
    c=[]
    for i in a:
        c.append(i[::-1])
    return c





d=input()
d=d.split()
print(*po(d))