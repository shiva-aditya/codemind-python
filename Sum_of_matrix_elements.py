r=int(input())
c=int(input())
d=[]
for i in range(r):
    d=d+list(map(int,input().split()))
print(sum(d))