def po(a,l):
    ans=[]
    for i in range(0,l):
        ans.append(a[i]*a[i])
    return sorted(ans)





s=int(input())
p=list(map(int,input().split()))
print(*po(p,s))