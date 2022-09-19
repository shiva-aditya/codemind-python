def po(D,d,P,Q):
    c=0
    for i in range(0,D//d):
        c=c+(d*(P+(i*Q)))
    if (D%d)==0:
        return c
    else:
        c=c+((D%d)*(P+((D//d)*Q)))
    return c
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    print(po(a,b,c,d))