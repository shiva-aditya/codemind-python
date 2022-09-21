def po(l,r,k):
    c=0
    for i in range(l,r+1):
        if i%k==0:
            c+=1
    return c
a,b,c=map(int,input().split())
print(po(a,b,c))