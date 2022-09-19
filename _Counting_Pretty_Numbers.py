def po(a,b):
    c=0
    for i in range(a,b+1):
        d=list(str(i))
        if d[-1]=="2" or d[-1]=="3" or d[-1]=="5":
            c+=1
    return c
for _ in range(int(input())):
    t,n=map(int,input().split())
    print(po(t,n))