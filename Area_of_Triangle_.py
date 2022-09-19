def po(a,b,c):
    s=(a+b+c)/2
    y=(s*(s-a)*(s-b)*(s-c))**0.5
    return y
n,m,o=list(map(int,input().split()))
y=po(n,m,o)
print("%.2f"%y)