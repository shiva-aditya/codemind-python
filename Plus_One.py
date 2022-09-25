b=int(input())
a=list(map(int,input().split()))
d=""
for i in range(b):
    d=d+str(a[i])
w=str(int(d)+1)
for j in w:
    print(j,end=" ")
            



