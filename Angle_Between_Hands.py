b,c=map(int,input().split(":"))
a=6*c
d=(30*b)+(0.5*c)
f=abs(a-d)
if f>180:
    print(360-f)
else:
    print(f)