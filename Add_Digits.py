def po(a):
    f=0
    while a:
        d=a%10
        a=a//10
        f+=d
    if len(str(f))>1:
        return po(f)
    else:
        return f
f=int(input())
print(po(f))