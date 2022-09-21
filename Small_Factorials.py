def po(a):
    c=1
    for i in range(1,a+1):
        c=c*i
    return c
for _ in range(int(input())):
    d=int(input())
    print(po(d))