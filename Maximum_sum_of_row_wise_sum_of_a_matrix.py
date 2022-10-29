def po(n):
    ans=[]
    for i in n:
        ans.append(sum(i))
    return max(ans)





p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
print(po(a))