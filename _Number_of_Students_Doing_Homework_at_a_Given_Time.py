def po(n,m,q):
    c=0
    for i in range(0,len(n)):
        d=[]
        for j in range(n[i],m[i]+1):
            d.append(j)
        if q in d:
            c+=1
    return c
    
n=int(input())
f=list(map(int,input().split()))
m=int(input())
s=list(map(int,input().split()))
q=int(input())
print(po(f,s,q))