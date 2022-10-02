def po(a,l):
    for i in range(0,l):
        if i==0:
            if sum(a[i+1::])==0:
                return "YES"
        elif i==l-1:
            continue
        else:
            x=a[i+1::]
            y=a[i-1::-1]
            if sum(x)==sum(y):
                return "YES"
    return "NO"
            

for _ in range(int(input())):  
    f=int(input())
    d=list(map(int,input().split()))
    print(po(d,f))
