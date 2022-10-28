summ=0
d=[]
n,m=map(int,input().split())
for _ in range(n):
    a=list(map(int,input().split()))
    summ+=sum(a)
print(summ)