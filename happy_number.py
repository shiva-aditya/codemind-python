def po(a):
    c=0
    while a:
        d=a%10
        a=a//10
        c=c+(d*d)
    if len(str(c))>1:
        return po(int(c))
    else:
        return int(c)

k=int(input())
p=po(k)
if p==1 or p==7:
    print(True)
else:
    print(False)