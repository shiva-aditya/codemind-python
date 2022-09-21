def po(a):
    e=[]
    while a:
        f=a%10
        a=a//10
        e.append(f)
    c=0
    for i in e:
        t=mo(i)
        c=c+t
    return c
def mo(a):
    if a==0:
        return 1
    c=1
    for i in range(1,a+1):
        c=c*i
    return c
    
s=int(input())
h=po(s)
if h==s:
    print("The number",s,"is a strong number")
else:
    print("The number",s,"is not a strong number")