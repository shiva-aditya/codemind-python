def po(a,l):
    ans=[]
    for i in range(0,l):
        if a.count(a[i])==1:
            ans.append(a[i])
    if len(ans)>0:
        return max(ans)
    else:
        return -1




s=int(input())
n=list(map(int,input().split()))
print(po(n,s))