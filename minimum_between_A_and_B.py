def po(a,n,m):
    c=[]
    for i in range(n,m+1):
        c.append(i)
    ans=[]
    for i in a:
        if i in c:
            ans.append(i)
    if len(ans)==0:
        return -1
    else:
        return min(ans)


s=int(input())
q=list(map(int,input().split()))
n,m=map(int,input().split())
print(po(q,n,m))