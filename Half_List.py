def po(a,b):
    l=a[::-1]#6 7 8 3 4 5
    f=l[:(b//2):]#6 7 8
    a=a[:(b//2):]# 3 4 5
    f.extend(a)
    return f
    
    
g=int(input())
d=list(map(int,input().split()))
print(*po(d,g))
