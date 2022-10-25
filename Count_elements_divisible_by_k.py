def po(a,q):
    c=0
    for i in a:
        if i%q==0:
            c+=1
    return c







l,k=map(int,input().split())
q=list(map(int,input().split()))
print(po(q,k))