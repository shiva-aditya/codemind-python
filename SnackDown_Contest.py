def po(n,m,t):
    n=set(n[1::])
    m=set(m[1::])
    a=n.union(m)
    if len(a)>=t:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    print(po(p,q,n))