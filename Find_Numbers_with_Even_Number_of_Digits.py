def po(a,l):
    c=0
    for i in a:
        s=str(i)
        if len(s)%2==0:
            c+=1
    return c
            

d=int(input())
q=list(map(int,input().split()))
print(po(q,d))