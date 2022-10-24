def po(n,q):
    q=n.index(q)
    c=0
    for i in range(0,q+1):
        c+=n[i]
    return c


s=int(input())
q=list(map(int,input().split()))
a=int(input())
print(po(q,a))