def po(n,m):
    a,b=[],[]
    for i in range(len(n)):
        if n[i]!="#":
            a.append(n[i])
        else:
            a.remove(a[-1])

    for i in range(len(m)):
        if m[i]!="#":
            b.append(m[i])
        else:
            b.remove(b[-1])
            
    return a==b
    
a=input()
b=input()
print(po(a,b))