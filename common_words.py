def po(n,m):
    c=[]
    for i in range(len(m)):
        if m[i]in n:
            c.append(m[i])
    return c


a=input()
a=a.lower()
a=a.split()
b=input()
b=b.lower()
b=b.split()
print(*po(a,b))