def po(p,r,t):
    f=1+(r/100)
    g=f**t
    a=p*g
    return a
a,b,c=map(int,input().split())
d=po(a,b,c)
print("{:.2f}".format(d))