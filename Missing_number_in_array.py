def po(n,a):
    b=[]
    for i in range(1,n+1):
        b.append(i)
    q=set(a)
    x=set(b)
    d=x-q
    return d


for _ in range(int(input())):
    f=int(input())
    g=list(map(int,input().split()))
    print(*po(f,g))