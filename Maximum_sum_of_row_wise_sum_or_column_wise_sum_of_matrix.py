def po(n,r):
    ans=[]
    for i in range(r):
        summ=0
        for j in n:
            summ+=j[i]
        ans.append(summ)
    for i in n:
        ans.append(sum(i))
    return max(ans)
        
p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
print(po(a,l))