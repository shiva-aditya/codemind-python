def po(n):
    s=0
    for i in range(1,len(n)-1):
        w=sum(n[i])-n[i][0]-n[i][-1]
        s+=w
    return s

a=[]    
p,l=map(int,input().split())
for i in range(p):
    q=list(map(int,input().split()))
    a.append(q)
print(po(a))