def po(e,r):
    a=[]
    for i in e:
        if i not in a:
            a.append(i)
    b=[]
    for j in r:
        if j not in b:
            b.append(j)
    ans=[]
    for i in a:
        if i in b:
            ans.append(i)
    return ans

a,b=map(int,input().split())
k=list(map(int,input().split()))
q=list(map(int,input().split()))
print(*po(k,q))