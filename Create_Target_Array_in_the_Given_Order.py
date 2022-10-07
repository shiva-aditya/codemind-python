def po(n,m):
    ans=[]
    for i in range(0,len(n)):
        ans.insert(m[i],n[i])
    return ans



s=int(input())
n=list(map(int,input().split()))
l=int(input())
i=list(map(int,input().split()))
print(*po(n,i))