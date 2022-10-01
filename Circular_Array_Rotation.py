def fo(a,r):
    g=a[:abs(len(a)-r):]
    d=[]
    a.reverse()
    for i in range(0,len(a)):
        if i==r:
            break
        else:
            d.append(a[i])
    d.reverse()
    d.extend(g)
    return d

n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
s=fo(arr,k)
for _ in range(q):
    u=int(input())
    print(s[u])