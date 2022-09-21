a=int(input())
d=2**a
g=2**(a-1)
for j in range(0,g):
    f=list(bin(j))
    b=f[2::]
    for v in range(a-len(b)):
        b.insert(0,"0")
    r=""
    for t in b:
        r=r+t
    print(r)
for i in range(g,d):
    f=bin(i)
    print(f[2::])