def po(a):
    c=[]
    for i in a:
        c.append(len(i))
    return min(c)



u=input()
u=u.split()
print(po(u))