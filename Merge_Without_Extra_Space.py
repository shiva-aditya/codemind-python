def po(a,b):
    a.extend(b)
    a.sort()
    return a









for _ in  range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(*po(a,b))