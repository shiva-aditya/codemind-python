def po(n,m):
    c=0
    for j in n:
        if j>m:
            c=c+2
        else:
            c=c+1
    return c       
q=[]         
n=int(input())
for _ in range(n):
    g=int(input())
    q.append(g)
t=int(input())
print(po(q,t))
    