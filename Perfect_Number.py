def po(a):
    f=[]
    for i in range(1,a):
        if a%i==0:
            f.append(i)
    c=0
    for j in f:
        c=c+j
    if c==a:
        return True
    else:
        return False
g=int(input())
print(po(g))