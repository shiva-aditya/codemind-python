def po(a):
    c=0
    for i in range(1,a):
        if a%i==0:
            c=c+i
    return c>a
f=int(input())
print(po(f))