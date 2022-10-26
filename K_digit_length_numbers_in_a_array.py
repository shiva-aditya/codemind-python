def po(a,q):
    c=0
    for i in a:
        if len(str(abs(i)))==q:
            c+=1
    return c






s,l=map(int,input().split())
q=list(map(int,input().split()))
print(po(q,l))