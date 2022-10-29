def po(n):
    s=sum(n[0])+sum(n[-1])
    for i in range(1,len(n)-1):
        s+=n[i][0]+n[i][-1]
    return s



p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
print(po(a))