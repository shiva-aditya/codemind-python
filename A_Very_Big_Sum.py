def po(a):
    c=0
    for i in a:
        c=c+i
    return c





n=int(input())
p=list(map(int,input().split()))
print(po(p))