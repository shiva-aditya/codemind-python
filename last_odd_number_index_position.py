d=int(input())
f=list(map(int,input().split()))
for i in range(d-1,-1,-1):
    if f[i]%2!=0:
        print(i)
        break
    