def po(a):
    f=[0,1]
    c=0
    for i in range(2,a):
        v=f[::-1]
        c=v[0]+v[1]
        f.append(c)
    return f
g=int(input())
print(*(po(g)))