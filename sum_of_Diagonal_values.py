def po(n):
    summ=0
    for i in range(len(n)):
        summ+=a[i][i]
        #print(summ)
    for j in range(len(n)-1,-1,-1):
        summ+=a[i-j][j]
        #print(summ)
    return summ            

p,l=map(int,input().split())
a=[]
for i in range(p):
    f=list(map(int,input().split()))
    a.append(f)
if p%2==0:
    print(po(a))
else:
    print(po(a)-a[p//2][p//2])