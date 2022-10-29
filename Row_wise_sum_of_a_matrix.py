def po(n):
    ans=[]
    for i in n:
        print(sum(i),end=" ")





p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
po(a)