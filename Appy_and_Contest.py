def po(n,a,b,k):
    c=0
    for i in range(1,n+1):
        if i%a==0 or i%b==0:
            if i%a==0 and i%b==0:
                continue
            else:
                c+=1
        if c==k:
            return "Win"
    return "Lose"
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    print(po(a,b,c,d))            