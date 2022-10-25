def po(a,q):
    c=0
    for i in a:
        if i%q!=0:
            c+=1
    return c
    






q,k=map(int,input().split())
p=list(map(int,input().split()))
print(po(p,k))